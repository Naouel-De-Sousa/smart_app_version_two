import pandas as pd
from app import *
from utilities.format_data import build_dict_convert_df
import numpy as np
import pandas.api.types as ptypes


    
# test that out put is dataframe

def test_build_dict_convert_df():
    simulation_one = { 'masse':22000,
    'NZ1':0.03,
    'PITCH_1':5, 
    'ROLL_1':1.66, 
     'Vx_GRD':48.5,
    'Delta_Ny_AC':0.0,
    'Wy_AC':0.0,
     'Wx_AC':-3.6,
    'time_nz_max':0.11,
    'delta_pitch':-0.7,
    'delta_roll':0.06,
    'delta_nz':1.13}

    df_test= pd.DataFrame(np.eye(12))
    test_type = type(df_test)
    
    result_test_function = build_dict_convert_df(simulation_one)
    assert type(result_test_function) == test_type



# test columns name 
def test_columns_name():
    col_test_simulation_two = [ 'masse',
    'NZ1',
    'PITCH_1', 
    'ROLL_1', 
    'Vx_GRD',
    'Delta_Ny_AC',
    'Wy_AC',
    'Wx_AC',
    'time_nz_max',
    'delta_pitch',
    'delta_roll',
    'delta_nz']
    df_test = build_dict_convert_df()
    assert (df_test.columns.to_list()) == col_test_simulation_two

# test first columns name
def test_columns_name():
    test_first_col = ['masse']
    df_test_first = build_dict_convert_df()
    assert (df_test_first.columns.to_list[0]) == test_first_col

               
# t =pd.DataFrame(np.eye(12))
# cols_to_check = [ 'masse',
#     'NZ1',
#     'PITCH_1', 
#     'ROLL_1', 
#     'Vx_GRD',
#     'Delta_Ny_AC',
#     'Wy_AC',
#     'Wx_AC',
#     'time_nz_max',
#     'delta_pitch',
#     'delta_roll',
#     'delta_nz']

# assert all(ptypes.is_numeric_dtype(t[col]) for col in cols_to_check)
# # True
# assert ptypes.is_string_dtype(t['masse'])
# # True
# assert ptypes.is_datetime64_any_dtype(t['NZ1'])
   

    
    
  
