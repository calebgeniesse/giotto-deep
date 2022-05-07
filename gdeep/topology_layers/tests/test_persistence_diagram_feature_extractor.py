from typing import Tuple, List

import numpy as np


from gdeep.topology_layers.persistence_diagram_feature_extractor \
    import PersistenceDiagramFeatureExtractor
    
def test_persistence_diagram_feature_extractor():
    diagrams = []

    diagrams.append(
        np.array(
            [[0.08348271, 0.22057831, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08348271, 0.22057831, 1.        , 0.        , 0.        ,
            0.        ],
        [0.07321328, 0.09998664, 1.        , 0.        , 0.        ,
            0.        ],
        [0.07447072, 0.09998664, 1.        , 0.        , 0.        ,
            0.        ],
        [0.09821013, 0.11540078, 1.        , 0.        , 0.        ,
            0.        ],
        [0.09202451, 0.10274777, 1.        , 0.        , 0.        ,
            0.        ],
        [0.07220701, 0.22057831, 0.        , 1.        , 0.        ,
            0.        ],
        [0.07321328, 0.11662579, 0.        , 0.        , 1.        ,
            0.        ],
        [0.09821013, 0.11540078, 0.        , 0.        , 1.        ,
            0.        ],
        [0.09314044, 0.09998664, 0.        , 0.        , 1.        ,
            0.        ],
        [0.07447072, 0.11662579, 0.        , 0.        , 0.        ,
            1.        ],
        [0.07220701, 0.13467948, 0.        , 0.        , 0.        ,
            1.        ],
        [0.09202451, 0.11662579, 0.        , 0.        , 0.        ,
            1.        ]]
        )
    )

    diagrams.append(
        np.array(
            [[0.08041324, 0.20871319, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08041324, 0.20871319, 1.        , 0.        , 0.        ,
            0.        ],
        [0.06630885, 0.08221929, 1.        , 0.        , 0.        ,
            0.        ],
        [0.06735194, 0.07515375, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08542901, 0.0928795 , 1.        , 0.        , 0.        ,
            0.        ],
        [0.07839674, 0.08220349, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08826917, 0.09014139, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08815335, 0.08928269, 1.        , 0.        , 0.        ,
            0.        ],
        [0.06454494, 0.20871319, 0.        , 1.        , 0.        ,
            0.        ],
        [0.06735194, 0.1108973 , 0.        , 0.        , 1.        ,
            0.        ],
        [0.07839674, 0.1011092 , 0.        , 0.        , 1.        ,
            0.        ],
        [0.08542901, 0.0928795 , 0.        , 0.        , 1.        ,
            0.        ],
        [0.08826917, 0.09014139, 0.        , 0.        , 1.        ,
            0.        ],
        [0.06735194, 0.09014139, 0.        , 0.        , 0.        ,
            1.        ],
        [0.06630885, 0.1011092 , 0.        , 0.        , 0.        ,
            1.        ],
        [0.07399798, 0.1011092 , 0.        , 0.        , 0.        ,
            1.        ],
        [0.06454494, 0.11253277, 0.        , 0.        , 0.        ,
            1.        ],
        [0.08815335, 0.1108973 , 0.        , 0.        , 0.        ,
            1.        ]]
        )
    )

    diagrams.append(
        np.array(
            [[0.08254243, 0.21609358, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08254246, 0.21609358, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08254011, 0.21608838, 1.        , 0.        , 0.        ,
            0.        ],
        [0.08254012, 0.21608838, 1.        , 0.        , 0.        ,
            0.        ],
        [0.07942715, 0.20433015, 1.        , 0.        , 0.        ,
            0.        ],
        [0.07942715, 0.20433015, 1.        , 0.        , 0.        ,
            0.        ],
        [0.07942406, 0.20432301, 1.        , 0.        , 0.        ,
            0.        ],
        [0.0794241 , 0.20432301, 1.        , 0.        , 0.        ,
            0.        ],
        [0.06248347, 0.10307311, 1.        , 0.        , 0.        ,
            0.        ],
        [0.06632324, 0.1017696 , 1.        , 0.        , 0.        ,
            0.        ],
        [0.06632368, 0.10176831, 1.        , 0.        , 0.        ,
            0.        ],
        [0.06248348, 0.08319741, 1.        , 0.        , 0.        ,
            0.        ],
        [0.07045262, 0.0831973 , 1.        , 0.        , 0.        ,
            0.        ],
        [0.04254924, 0.21609358, 0.        , 1.        , 0.        ,
            0.        ],
        [0.06632324, 0.21608838, 0.        , 0.        , 1.        ,
            0.        ],
        [0.06632368, 0.20433015, 0.        , 0.        , 1.        ,
            0.        ],
        [0.07045262, 0.20432301, 0.        , 0.        , 1.        ,
            0.        ],
        [0.07045279, 0.10307311, 0.        , 0.        , 1.        ,
            0.        ],
        [0.07045262, 0.10307311, 0.        , 0.        , 0.        ,
            1.        ],
        [0.06248347, 0.12018182, 0.        , 0.        , 0.        ,
            1.        ],
        [0.06248348, 0.12018248, 0.        , 0.        , 0.        ,
            1.        ]]
        )
    )

    diagram_shapes: List[Tuple[int,...]] = [diagram.shape for diagram in diagrams]

    mean = np.array([[0.5, 0.5],
                    [0.3, 2.0],
                    [0.5, 0.5],
                    [1.0, 1.0]])
    std = np.array([[0.1, 0.1],
                    [3.1, 2.2],
                    [0.1, 0.1],
                    [0.1, 0.1]])
    pd_extractor = PersistenceDiagramFeatureExtractor(
        mean=mean,
        std=std,
        number_of_homology_dimensions=4,
        number_of_most_persistent_features=3,
    )

    features = pd_extractor(diagrams)


    assert features['attention_mask'].shape == (3, 3)
    assert features['input_values'].shape == (3, 3, 6)

    assert np.allclose(
    features['input_values'][0][np.where(features['input_values'][0, :, 2 + 1] == 1)][:, :2],
    np.array([[(0.07220701 - 0.3)/ 3.1, 
            (0.22057831 - 2.0) / 2.2
            ]])
    )

# %%
from gdeep.topology_layers import PersistenceDiagramFeatureExtractor
from gdeep.utility.constants import DEFAULT_DATA_DIR


persistence_diagrams = np.random.rand(2, 10, 2)

mean = np.array([[0.5, 0.5]])
std = np.array([[0.1, 0.1]])

pd_extractor = PersistenceDiagramFeatureExtractor(
    mean=mean,
    std=std,
    number_of_homology_dimensions=1,
    number_of_most_persistent_features=3,
)


features = pd_extractor(persistence_diagrams)

input_values = features['input_values']
attention_masks = features['attention_mask']
# %%
