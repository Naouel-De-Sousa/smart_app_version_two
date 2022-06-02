import pandas as pd


# list_of_feature :
# masse = "",NZ1 = "",PITCH_1 = "",ROLL_1= "", Vx_GRD = "" Delta_Ny_AC = "",Wy_AC = ""Wx_AC ="",time_nz_max ="",delta_pitch = "",delta_roll = "",delta_nz =""
def build_dict_convert_df(masse = "",NZ1 = "",PITCH_1 = "",
                            ROLL_1= "", 
                            Vx_GRD = "",
                            Delta_Ny_AC = "",
                            Wy_AC = "",
                            Wx_AC ="",
                            time_nz_max ="",
                            delta_pitch = "",
                            delta_roll = "",
                            delta_nz =""):
    data = { 'masse':[masse],
        'NZ1':[NZ1], 
        'PITCH_1':[PITCH_1], 
        'ROLL_1':[ROLL_1], 
        'Vx_GRD':[Vx_GRD],
        'Delta_Ny_AC':[Delta_Ny_AC],
        'Wy_AC':[Wy_AC],
        'Wx_AC':[Wx_AC],
        'time_nz_max':[time_nz_max],
        'delta_pitch':[delta_pitch],
        'delta_roll':[delta_roll],
        'delta_nz':[delta_nz]}
                                    
    features = pd.DataFrame(data)
    return features


