Search.setIndex({docnames:["index","installation","modules/analysis","modules/bert","modules/data","modules/index","modules/models","modules/pipeline","modules/search","modules/topology_layers","modules/utility","modules/visualisation"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["index.rst","installation.rst","modules/analysis.rst","modules/bert.rst","modules/data.rst","modules/index.rst","modules/models.rst","modules/pipeline.rst","modules/search.rst","modules/topology_layers.rst","modules/utility.rst","modules/visualisation.rst"],objects:{"gdeep.analysis":[[2,0,0,"-","decision_boundary"],[2,0,0,"-","interpretability"]],"gdeep.analysis.decision_boundary":[[2,1,1,"","DecisionBoundaryCalculator"],[2,1,1,"","GradientFlowDecisionBoundaryCalculator"],[2,1,1,"","QuasihyperbolicDecisionBoundaryCalculator"],[2,1,1,"","UniformlySampledPoint"]],"gdeep.analysis.decision_boundary.DecisionBoundaryCalculator":[[2,2,1,"","get_decision_boundary"],[2,2,1,"","step"]],"gdeep.analysis.decision_boundary.GradientFlowDecisionBoundaryCalculator":[[2,2,1,"","get_decision_boundary"],[2,2,1,"","step"]],"gdeep.analysis.decision_boundary.QuasihyperbolicDecisionBoundaryCalculator":[[2,2,1,"","get_decision_boundary"],[2,2,1,"","step"]],"gdeep.analysis.decision_boundary.UniformlySampledPoint":[[2,2,1,"","get_dim"]],"gdeep.analysis.interpretability":[[2,1,1,"","Interpreter"]],"gdeep.analysis.interpretability.Interpreter":[[2,2,1,"","interpret_image"],[2,2,1,"","interpret_tabular"],[2,2,1,"","interpret_text"]],"gdeep.bert":[[3,1,1,"","SimplifiedBertBlock"],[3,1,1,"","SimplifiedBertClassifier"],[3,1,1,"","SimplifiedBertEmbeddings"],[3,1,1,"","SimplifiedBertEncoder"],[3,1,1,"","SimplifiedBertPooler"],[3,1,1,"","SimplifiedMultiHeadSelfAttention"]],"gdeep.bert.SimplifiedBertBlock":[[3,2,1,"","forward"]],"gdeep.bert.SimplifiedBertClassifier":[[3,2,1,"","forward"]],"gdeep.bert.SimplifiedBertEmbeddings":[[3,2,1,"","forward"]],"gdeep.bert.SimplifiedBertEncoder":[[3,2,1,"","forward"]],"gdeep.bert.SimplifiedBertPooler":[[3,2,1,"","forward"]],"gdeep.bert.SimplifiedMultiHeadSelfAttention":[[3,2,1,"","forward"]],"gdeep.data":[[4,1,1,"","CreateToriDataset"],[4,1,1,"","DataLoaderFromArray"],[4,1,1,"","DataLoaderFromImages"],[4,1,1,"","DataLoaderKwargs"],[4,1,1,"","GenericDataset"],[4,1,1,"","OrbitsGenerator"],[4,1,1,"","PreprocessText"],[4,1,1,"","PreprocessTextTranslation"],[4,1,1,"","Rotation"],[4,1,1,"","TextDataset"],[4,1,1,"","TextDatasetTranslation"],[4,1,1,"","TorchDataLoader"],[4,3,1,"","create_pd_orbits"],[4,3,1,"","generate_orbit_parallel"]],"gdeep.data.CreateToriDataset":[[4,2,1,"","generate_dataset"]],"gdeep.data.DataLoaderFromArray":[[4,2,1,"","build_dataloaders"]],"gdeep.data.DataLoaderFromImages":[[4,2,1,"","build_dataloaders"]],"gdeep.data.OrbitsGenerator":[[4,2,1,"","get_dataloader_combined"],[4,2,1,"","get_dataloader_orbits"],[4,2,1,"","get_dataloader_persistence_diagrams"],[4,2,1,"","get_orbits"],[4,2,1,"","get_persistence_diagrams"]],"gdeep.data.PreprocessText":[[4,2,1,"","build_dataloaders"]],"gdeep.data.PreprocessTextTranslation":[[4,2,1,"","build_dataloaders"]],"gdeep.data.TorchDataLoader":[[4,2,1,"","build_dataloaders"]],"gdeep.models":[[6,1,1,"","FFNet"],[6,1,1,"","ModelExtractor"],[6,1,1,"","PeriodicNeuralNetwork"],[6,1,1,"","SaveLayerOutput"],[6,1,1,"","SaveNodeOutput"],[6,1,1,"","SaveOutput"]],"gdeep.models.FFNet":[[6,2,1,"","forward"]],"gdeep.models.ModelExtractor":[[6,2,1,"","get_activations"],[6,2,1,"","get_decision_boundary"],[6,2,1,"","get_gradients"],[6,2,1,"","get_layers_grads"],[6,2,1,"","get_layers_param"]],"gdeep.models.PeriodicNeuralNetwork":[[6,2,1,"","forward"]],"gdeep.pipeline":[[7,1,1,"","Pipeline"]],"gdeep.pipeline.Pipeline":[[7,2,1,"","copy_dataloader_params"],[7,2,1,"","evaluate_classification"],[7,2,1,"","parallel_tpu_training_loops"],[7,2,1,"","register_pipe_hook"],[7,2,1,"","train"]],"gdeep.search":[[8,1,1,"","Benchmark"],[8,1,1,"","Gridsearch"]],"gdeep.search.Benchmark":[[8,2,1,"","start"]],"gdeep.search.Gridsearch":[[8,2,1,"","start"]],"gdeep.topology_layers":[[9,1,1,"","FastAttention"],[9,1,1,"","GraphClassifier"],[9,1,1,"","ISAB"],[9,1,1,"","PMA"],[9,1,1,"","Persformer"],[9,1,1,"","SAB"]],"gdeep.topology_layers.FastAttention":[[9,2,1,"","forward"]],"gdeep.topology_layers.GraphClassifier":[[9,2,1,"","forward"]],"gdeep.topology_layers.ISAB":[[9,2,1,"","forward"]],"gdeep.topology_layers.PMA":[[9,2,1,"","forward"]],"gdeep.topology_layers.Persformer":[[9,2,1,"","forward"],[9,4,1,"","num_params"]],"gdeep.topology_layers.SAB":[[9,2,1,"","forward"]],"gdeep.utility":[[10,3,1,"","ensemble_wrapper"],[10,3,1,"","save_model_and_optimizer"]],"gdeep.visualisation":[[11,1,1,"","Compactification"],[11,1,1,"","Visualiser"],[11,3,1,"","persistence_diagrams_of_activations"],[11,3,1,"","plotly2tensor"]],"gdeep.visualisation.Compactification":[[11,2,1,"","create_final_distance_matrix"],[11,2,1,"","plot_chart"]],"gdeep.visualisation.Visualiser":[[11,2,1,"","betti_plot_layers"],[11,2,1,"","plot_activations"],[11,2,1,"","plot_data_model"],[11,2,1,"","plot_decision_boundary"],[11,2,1,"","plot_interpreter_image"],[11,2,1,"","plot_interpreter_tabular"],[11,2,1,"","plot_interpreter_text"],[11,2,1,"","plot_persistence_diagrams"]],gdeep:[[3,0,0,"-","bert"],[4,0,0,"-","data"],[6,0,0,"-","models"],[7,0,0,"-","pipeline"],[8,0,0,"-","search"],[9,0,0,"-","topology_layers"],[10,0,0,"-","utility"],[11,0,0,"-","visualisation"]]},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"],"4":["py","property","Python property"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function","4":"py:property"},terms:{"0":[2,4,6,7,8,9,11],"001":[7,8],"05":11,"1":[1,2,4,6,8,9,11],"10":[7,8,11],"100":[4,6],"1000":[2,4,11],"128":[4,9],"15210":9,"19":1,"1d":6,"2":[3,4,6,9],"2019":9,"2112":9,"2darrai":7,"2f4fe03d77724a7217006e5d16728874":9,"3":[1,4,6,9],"32":[7,8,9],"4":[1,4,9,11],"5":[1,4,7,8,9,11],"50":9,"5000":11,"6":[1,9],"64":9,"7":2,"8":9,"abstract":2,"boolean":[7,8],"class":[2,3,4,6,7,8,9,10,11],"default":[2,3,4,6,7,8,9,11],"do":10,"final":6,"float":[2,4,6,7,9,11],"function":[2,3,4,6,7,8,9,10,11],"int":[2,3,4,6,7,8,9,11],"return":[2,3,4,6,7,9,11],"static":7,"true":[6,9],"while":[3,4,6,9],A:[8,9,11],By:4,For:8,If:[1,7,8],In:4,It:[2,3,4,8,11],On:7,The:[1,4,6,7,9,10],Then:10,These:9,To:6,_variablefunctionsclass:3,ab:9,abov:1,absolut:3,account:7,accross:11,accumul:[7,8],accuraci:[7,8],act:4,activ:[2,6,7,8,9,11],activations_list:11,actual:7,adapt:6,add:4,addit:[4,9],after:[1,7],afterward:[3,6,9],ai:[1,2],all:[1,3,4,6,7,9,11],allow:[7,8,11],alpha:[4,11],also:1,although:[3,6,9],an:[2,4,6,8,11],analysi:[0,3,5,11],angl:4,api:0,appli:3,ar:[4,7,9],arbitrary_precis:4,arch:6,architectur:[7,9],arg:[2,3,4,6,7,8,9,10,11],argument:[2,4,6,7,10,11],arrai:[4,6,11],arxiv:9,attent:[3,9],attention_mask:3,attention_typ:9,attribut:2,automat:1,avail:[1,4,5],averag:[6,7],axi:2,axis_0:4,axis_1:4,b:2,base:[2,4,9],bash:1,batch:[3,6,7],batch_siz:[7,8],bechmark:8,been:4,befor:1,belong:2,benchhmark:7,benchmark:8,bert:[0,5],bertconfig:3,best:8,best_not_last:8,better:11,betti:11,betti_plot_lay:11,bh:1,bia:9,bias:6,bias_attent:9,blob:9,block:[3,9],bool:[4,7,8,11],both:1,bound:2,boundari:[2,6,11],boundary_list:6,boundary_tupl:11,box:2,bridg:11,build:[4,6],build_dataload:4,built:6,c:2,calcul:2,call:[3,4,6,7,8,9,11],callabl:[2,4,6,7,8],can:[1,2,4,6,8,10],captum:2,care:[3,6,9],cc:9,cd:1,chang:1,chart:11,check:[2,4],check_optuna:7,choos:11,chosen:4,cl:3,classic:4,classical_convent:4,classif:[3,4,9],classifi:[3,9],clone:1,close:11,cloud:[2,4],clss:10,code:7,colab:7,column:4,com:[1,9],command:1,compact:11,compactif:11,compactifi:11,complex:[9,11],comput:[2,3,4,6,8,9,11],concaten:[3,9],config:3,configuration_bert:3,confus:7,connect:[8,9],consid:8,consist:[3,4],contain:[4,5,6],convent:4,convert:[4,11],convert_to_map_dataset:4,coordin:[4,11],copy_dataloader_param:7,core:7,correspond:[2,3,6,7,9],correspondign:2,cpu:4,cpu_count:4,creat:[2,6],create_final_distance_matrix:11,create_pd_orbit:4,createtoridataset:4,criterion:7,cross:[7,8],cross_valid:[7,8],crossvalid:8,csv:4,current:[2,7],curv:11,custom:6,customli:4,cycl:[6,7],d_in:2,d_out:2,data:[0,2,5,7,9,11],databas:8,dataload:[4,7,8],dataloaderfromarrai:4,dataloaderfromimag:4,dataloaderkwarg:4,dataloaders_dict:8,dataloaders_kwarg:4,dataloaders_param:[7,8],dataset:[4,7,8],db_name:8,db_url:8,decis:[2,6,11],decision_boundari:2,decisionboundarycalcul:2,decison:11,decod:9,deep:1,defin:[3,4,6,8,9,11],depend:[0,4],describ:9,descript:9,develop:0,diagram:[4,9,11],dict:[4,6,7,8],dictionari:[7,8],differ:[2,3,4,8,11],dim:[3,9],dim_head:9,dim_hidden:9,dim_in:9,dim_input:9,dim_out:9,dim_output:9,dimens:[2,4,6,9,11],dimensionwis:2,directli:4,directori:1,discretis:11,distanc:11,dl:7,dl_t:[7,8],dl_tr:[7,8],dl_tr_old:7,dl_val:7,dl_val_old:7,doe:2,domain:6,downstream:3,dropout:9,dropout_dec:9,dropout_enc:9,dtype:4,dure:8,dynam:4,dynamical_system:4,e:[1,6,7,8],each:[4,6,7,8,9,11],easili:6,edg:[6,11],effect:6,einop:3,either:[2,4,7,8,9],element:[4,9],elementari:6,eman:2,embed:3,encod:[3,9],ensembl:10,ensemble_wrapp:10,entri:6,environ:1,epoch:[7,8,11],epsilon:11,estim:[2,10],evalu:7,evaluate_classif:7,everi:[3,6,9],exampl:[1,6,8,10,11],except:6,exist:[7,8],expect:2,experiment:7,extract:[2,6],factor:6,fail:1,fals:[4,7,8,9,11],famili:4,fast:9,fast_transformer_pytorch:9,fastattent:9,featur:[5,6,9,11],feed:[3,6,9],ffnet:6,fig:11,figur:11,file:[4,9],filtrat:11,find:[2,6],first:[4,6],five:7,flag:[7,8],float32:4,flow:2,fold:[7,8],folder:4,form:11,former:[3,6,9],forward:[3,6,9],from:[1,3,4,6,7,8,11],full:9,fulli:9,g:[6,7,8],gdeep:[2,3,4,6,7,8,9,10,11],gelu:9,gener:[2,4,6,7,8],generate_dataset:4,generate_orbit_parallel:4,genericdataset:4,geodes:2,get:[3,11],get_activ:6,get_dataloader_combin:4,get_dataloader_orbit:4,get_dataloader_persistence_diagram:4,get_decision_boundari:[2,6],get_dim:2,get_gradi:6,get_layers_grad:6,get_layers_param:6,get_orbit:4,get_persistence_diagram:4,giotto:1,git:1,github:[1,9],given:[2,4,6],grad:6,gradient:[2,6,7,8],gradientflowdecisionboundarycalcul:2,graph:9,graphclassifi:9,graphicobject:11,gridsearch:[7,8],group:6,h:[2,4],ha:[4,6,8,11],hand:7,have:[4,6],head:[3,9],henc:4,hidden:9,homolog:[4,11],homology_dimens:[4,11],hook:[3,6,9],host:8,hot:3,how:11,html:4,http:[1,2,4,9],hypercub:6,hyperparamet:4,hypersurfac:11,i:11,ignor:[3,6,7,9],imag:[2,4,11],immedi:1,index:[0,5,11],indic:2,induc:9,induced_attent:9,info:[2,11],init:7,initial_point:2,initial_vector:2,initialis:[4,10],initilis:11,input:[2,3,6,9,11],input_dim:9,input_exampl:6,input_id:3,insid:[1,6],insight:11,instal:0,instanc:[3,6,7,8,9],instead:[3,6,9],integ:[4,8],integr:2,integratedgradi:2,interpret:[2,6,11],interpret_imag:2,interpret_tabular:2,interpret_text:2,intrins:11,isab:9,item:8,iterabledataset:4,its:11,jupyt:1,k:11,k_fold:[7,8],keep_train:[7,8],kei:[6,9],keyword:[4,6],kind:11,kwarg:[2,4,6],label:[2,4],labels_fil:4,last:[2,4,6,8],latest:1,latter:[3,6,9],launch:1,layer:[0,2,3,5,6,7,8,11],layer_norm:9,layer_norm_pool:9,layer_typ:11,layser:6,learn:[7,8,9],left:[8,11],length:11,librari:[1,5,10],like:[1,3,7,10],line:7,linear:[3,9],list:[2,4,5,6,7,8,11],ln:9,loader:[4,7],local:1,local_test:1,locat:4,logit:3,loss:[6,7,8],loss_fn:[6,7,8,11],lower:2,lr:[7,8],lr_schedul:[7,8],lucidrain:9,m:1,machin:[1,9],mai:1,main:[9,11],maion:4,make:[1,2,6],manner:4,map:2,mapdataset:4,mask:3,matplotlib:11,matrix:7,max_edge_length:11,maximum:11,medianprun:8,method:[2,4,7,8,11],metric:7,min_len:2,mnist:4,mode:11,model:[0,2,3,5,7,8,9,10,11],model_nam:10,modelextractor:[6,7],models_dict:8,models_hyperparam:8,models_param:7,modul:[0,2,3,5,6,7,8,9,10,11],more:2,multi:[3,8,9],multipl:8,multiprocess:4,mysql:8,mysqldb:8,n:[2,4],n_accumulated_grad:[7,8],n_epoch:[6,7,8,11],n_featur:[6,11],n_job:4,n_point:4,n_pt:4,n_sampl:[2,6,11],n_trial:8,name:[4,6,8,10],ndarrai:4,necessari:1,need:[3,6,9,11],neighbor:11,network:[2,6,11],neural:[2,6],neural_net:11,neurip:9,next:3,nn:[2,6,7,8,10,11],node:6,none:[2,3,4,7,8,10,11],norm:9,normal:[9,10],note:[1,4,7],now:3,np:4,nsgaiisampl:8,num_class:[4,7,9],num_featur:9,num_head:9,num_ind:9,num_label:3,num_layer_dec:9,num_layer_enc:9,num_orbit:4,num_orbits_per_class:4,num_output:9,num_param:9,num_persistence_point:4,num_pts_per_orbit:4,num_se:9,num_topological_featur:4,number:[2,4,6,7,8,9,11],number_of_step:2,numpi:[1,4],obj:8,object:[4,8],obtain:[1,4],old:1,onc:4,one:[3,4,6,7,9,11],onli:[3,7,8,10],optim:[2,7,8,10],optimis:7,optimizer_param:8,optimizers_param:[7,8],option:[2,3,4,9,10,11],optuna:[7,8],optuna_param:7,orbit:[4,6],orbitsgener:4,order:7,org:[4,9],origin:10,original_dataload:7,other:7,otherwis:11,ouput:8,output:[3,6,9,10],output_dim:9,over:[3,7,8],overridden:[3,6,9],page:5,pair:[6,11],paper:9,parallel:[4,7],parallel_orbit:4,parallel_tpu:[7,8],parallel_tpu_training_loop:7,param:[2,8],paramet:[4,6,7,8,9,11],pass:[3,4,6,9],path:4,pca:11,pdf:9,per:[4,11],percentag:4,perform:[2,3,6,7,8,9],period:6,periodicneuralnetwork:6,persform:9,persist:[4,9,11],persistence_diagrams_of_activ:11,ph:1,pip:1,pipe:11,pipelin:[0,4,5,8,11],plot:11,plot_activ:11,plot_chart:11,plot_data_model:11,plot_decision_boundari:11,plot_interpreter_imag:11,plot_interpreter_tabular:11,plot_interpreter_text:11,plot_persistence_diagram:11,plotli:11,plotly2tensor:11,pma:9,point:[2,4,6,11],pointcloud:6,pool:9,pooler:3,port:8,posit:[3,7,8],possibl:3,pp_convent:4,pre:9,pre_layer_norm:9,precis:[6,11],predict:[3,4],prepend:8,preprocess:4,preprocesstext:[2,4],preprocesstexttransl:4,present:11,probabl:[3,9],proceed:9,prof:7,profil:[7,8],properti:9,pruner:8,psw:8,pull:1,purpos:11,push:11,py:9,pypi:1,pytest:1,python:1,pytorch:[2,4,9],pytorch_self_attent:9,pytorch_self_attention_skip:9,quadrat:9,quasihyperbol:2,quasihyperbolicdecisionboundarycalcul:2,queri:9,r:4,rais:9,random:2,rate:[7,8],recent:1,recip:[3,6,9],recommend:1,reflect:6,region:6,regist:[3,6,7,9],register_pipe_hook:7,regularis:7,releas:1,relu:6,repres:11,represent:3,requir:[1,2,11],respect:2,restart:[7,8],result:[3,7,11],right:11,rotat:4,run:[1,3,4,6,7,8,9],s:[1,6],sab:9,saefli:7,salici:2,same:[1,4],sampl:[2,4,11],sampler:8,save:[6,10],save_model_and_optim:10,savelayeroutput:6,savenodeoutput:6,saveoutput:6,schduler:8,schedul:[7,8],scheduler_param:[7,8],schedulers_param:8,script:1,search:[0,5],search_metr:[7,8],second:4,see:9,self:[2,3,4,6,7,9,11],self_attent:9,send:11,sentenc:[2,3,4],sentiment:3,sequenc:4,set:9,setuptool:1,sever:8,sgd:7,shall:[4,11],shape:[2,3,4],should:[3,6,9],sigmoid:6,silent:[3,6,9],simplest:1,simplic:11,simplifi:[3,9],simplified_layer_norm:9,simplifiedbertblock:3,simplifiedbertclassifi:3,simplifiedbertembed:3,simplifiedbertencod:3,simplifiedbertpool:3,simplifiedmultiheadselfattent:3,sinc:[3,6,9],singl:[2,4,6,8,11],size:[2,4],skip:9,some:2,sourc:4,space:[6,11],specif:3,specifi:[2,6],stabl:[1,4],stack:3,standard:[2,6,7,8],start:8,state:[1,2],state_dict:10,step:[2,7],still:7,store:[4,6,7,8,11],store_grad_layer_hist:[7,8],str:[2,4,7,8,9,10],string:[2,4,7,8],studi:8,study_nam:8,subclass:[3,6,9],suit:1,sum:2,summarywrit:[7,8,11],support:6,surfac:11,system:4,tabular:11,tag:[7,8],take:[3,6,9],taken:7,taregt:4,target:[4,6],target_transform:4,task:[3,4],techniqu:2,tensor:[2,3,4,6,9,11],tensorboard:[7,8,11],test:[4,7],test_dataload:4,test_fold:4,test_kwarg:4,test_percentag:4,text:[4,11],textdataset:4,textdatasettransl:4,them:[1,3,6,9],thhe:[4,6],thi:[1,2,3,4,5,6,7,8,9,10,11],third:4,thu:4,token:[2,3,4],token_type_id:3,tokenis:4,tokenizer_lab:4,toler:11,topolog:[0,5,11],topology_lay:9,torch:[1,2,3,4,6,7,8,9,10,11],torchdataload:4,torchens:10,torchensebl:10,tori:4,toridatasset:4,toru:4,total:8,toward:2,tpesampl:8,tpu:[7,8],train:[4,6,7,8,11],train_kwarg:4,trainabl:[3,9],trainign:7,training_dataload:4,training_fold:4,transform:[3,4,9],translat:4,treat:4,trial:[7,8],tupl:[4,6,7,11],tuple_list:2,tutori:2,two:[4,8],type:[3,10,11],u:1,uniform:2,uniformlysampledpoint:2,unspecifi:8,up:3,upgrad:1,upper:2,us:[1,2,3,4,6,7,8,9],use_induced_attent:9,usebl:4,user:[0,7,8],usr:8,util:[0,4,5,7,8],val:4,val_kwarg:4,valid:[4,7,8],validation_percentag:4,valu:[2,4,7,8,9],valueerror:9,variabl:6,vector:9,veri:1,version:[1,11],via:[2,4],vision:4,visualis:[0,2,5],vocab:2,vocabulari:[2,4],votingclassifi:10,vr:11,w:[2,4],wai:1,want:[2,7,8],we:[1,2,7],weak:4,weight:[3,6],well:[7,8],when:8,where:4,wherev:3,whether:[4,7,8],which:[6,11],whole:9,wirter:7,wise:3,within:[3,6,9],without:11,word:3,work:3,would:10,wrap:[6,10],writer:[7,8,11],writer_tag:[7,8],x:[2,3,4,6,9],x_cont:6,x_featur:9,x_pd:9,x_test:[2,4],x_train:4,x_val:4,y:[2,4],y_train:4,y_val:4,you:[1,4,7,8,10],your:[1,6]},titles:["Welcome to giotto-deep\u2019s documentation!","Installation","Analysis","BERT","Data","API reference","Models","Pipeline","Search","Topology Layers","Utility","Visualisation"],titleterms:{To:1,analysi:2,api:5,bert:3,code:1,content:0,data:4,deep:0,depend:1,develop:1,document:0,giotto:0,instal:1,layer:9,model:6,pipelin:7,refer:[0,5],s:0,search:8,sourc:1,test:1,topolog:9,user:1,util:10,visualis:11,welcom:0}})