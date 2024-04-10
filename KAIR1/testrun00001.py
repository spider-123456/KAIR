from recbole.quick_start import run_recbole


# parameter_dict = {
#      'train_stage': 'finetune',
#      'pre_model_path': './saved/KAIR-Nov-07-2023_07-16-12.pth',
#      'train_neg_sample_args': None
# }

parameter_dict = {
    'train_stage': 'pretrain',
    'save_step': 1,
    'train_neg_sample_args': None
}

#parameter_dict = {
#   'train_neg_sample_args': None
#}

run_recbole(model='KAIR', dataset='ml-1m', config_dict=parameter_dict,config_file_list=['DATest.yaml'])

