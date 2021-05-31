from captum.attr import TokenReferenceBase, \
    visualization, FeatureAblation, \
    DeepLift, NoiseTunnel, IntegratedGradients, \
    LayerIntegratedGradients, Occlusion
import torch


class Interpreter:
    """Class to visualise the activation maps,
    the attribution maps and salicy maps using
    different techniques.

    Args:
        model (nn.Module):
        method (string): the interpretability method. Find
            more info [here](https://captum.ai/tutorials/)

        """

    def __init__(self, model,
                 method="IntegratedGradients"):
        self.model = model
        self.method = method
        self.stored_visualisations = []
        self.image = None
        self.X = None
        self.sentence = None
        self.attrib = None

    def interpret_image(self, X, y, **kwargs):
        occlusion = eval(self.method+"(self.model)")
        att = occlusion.attribute(X, target=y, **kwargs)
        self.image = X
        self.attrib = att
        return X, att

    def interpret_tabular(self, X_test, y, **kwargs):
        self.X = X_test  # eeded for plotting functions
        ig = IntegratedGradients(self.model)
        ig_nt = NoiseTunnel(ig)
        dl = DeepLift(self.model)
        # gs = GradientShap(self.model)
        fa = FeatureAblation(self.model)

        self.ig_attr_test = ig.attribute(X_test,
                                         n_steps=50,
                                         target=y,
                                         **kwargs)
        self.ig_nt_attr_test = ig_nt.attribute(X_test,
                                               target=y,
                                               **kwargs)
        self.dl_attr_test = dl.attribute(X_test,
                                         target=y,
                                         **kwargs)
        # self.gs_attr_test = gs.attribute(X_test, X_train, **kwargs)
        self.fa_attr_test = fa.attribute(X_test,
                                         **kwargs)

    def interpret_text(self, sentence, label, vocab,
                       tokenizer, layer,
                       min_len=7):
        self.sentence = sentence
        device = torch.device("cuda:0" if torch.cuda.is_available()
                              else "cpu")
        lig = eval(self.method+"(" + ",".join(("self.model", "self.model." +
                   layer)) + ")")
        text = tokenizer(sentence)
        if len(text) < min_len:
            text += ['.'] * (min_len - len(text))
        indexed = [vocab[t] for t in text]

        self.model.zero_grad()

        input_indices = torch.tensor(indexed)
        input_indices = input_indices.unsqueeze(0)

        # input_indices dim: [sequence_length]
        seq_length = min_len

        # predict
        pred_temp = torch.softmax(self.model(input_indices), 1)
        pred = torch.max(pred_temp)
        pred_ind = torch.argmax(pred_temp).item()
        # generate reference indices for each sample
        PAD_IND = vocab['.']
        token_reference = TokenReferenceBase(reference_token_idx=PAD_IND)
        reference_indices = \
            token_reference.generate_reference(seq_length,
                                               device).unsqueeze(0)
        # compute attributions and approximation
        # delta using layer integrated gradients
        attributions_ig, delta = lig.attribute(input_indices,
                                               reference_indices,
                                               target=label,
                                               n_steps=500,
                                               return_convergence_delta=True)

        print('pred: ', pred_ind, '(', '%.2f' % pred, ')',
              ', delta: ', abs(delta.item()))

        self.add_attributions_to_visualizer(attributions_ig, text, pred,
                                            pred_ind, label, delta.item(),
                                            self.stored_visualisations,
                                            vocab)

    @staticmethod
    def add_attributions_to_visualizer(attributions, text, pred, pred_ind,
                                       label, delta, vis_data_records,
                                       vocab):
        attributions = attributions.sum(dim=2).squeeze(0)
        attributions = attributions / torch.norm(attributions)
        attributions = attributions.cpu().detach().numpy()

        # storing couple samples in an array for visualization purposes
        vis_data_records.append(visualization.VisualizationDataRecord(
                                attributions,
                                pred,
                                str(pred_ind),
                                str(label),
                                "1",
                                attributions.sum(),
                                text,
                                delta))
