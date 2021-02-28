
import pandas as pd
from fonctions import *
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import locale


def get_dataSet_initial_state(business,review,user,tip,checkin):
    df_business = pd.read_csv("../data/csv/"+business+".csv", header=0,low_memory=False)
    df_review = pd.read_csv("../data/csv/"+review+".csv", header=0,low_memory=False)
    df_user = pd.read_csv("../data/csv/"+user+".csv", header=0,low_memory=False)
    df_tip = pd.read_csv("../data/csv/"+tip+".csv", header=0,low_memory=False)
    df_checkin = pd.read_csv("../data/csv/"+checkin+".csv", header=0,low_memory=False)


    data = {'File':  ['Business', 'Review', 'User', 'Tip', 'Checkin'], 'Records': [len(df_business), len(df_review), len(df_user), len(df_tip), len(df_checkin) ]}
    df_dataSet = pd.DataFrame (data, columns = ['File', 'Records' ])

    df_dataSet.to_csv("data_Set_Initial_State.csv")

    fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(aspect="equal"))
    p, tx, autotexts = plt.pie(df_dataSet['Records'], labels=df_dataSet['File'], autopct="")

    for i, a in enumerate(autotexts):
        a.set_text(locale.format('%d', df_dataSet['Records'][i], 1))

    ax.set_title("The composition of the datset")
    ax.legend(p, df_dataSet['File'], title="Files",loc="upper center",bbox_to_anchor=(1, 0, 0.5, 1))
    plt.axis('equal')
    plt.show()



def get_csv_files_for_null_columns_rate(input,output):

    df = pd.read_csv(input, header=0,low_memory=False)
    df = delete_empty_columns(df)
    serie = round(df.isnull().sum() * 100 / len(df),4)

    df_result = pd.DataFrame({'Column_Name':serie.index, 'Rate_of_empty_values':serie.values})

    # Ne garder que l'attribut de l'objet json
    def format_column_name(x):
        splited = x.split('.')
        if(len(splited) > 1):
            return splited[1]
        else:
	        return x

    df_result['Column_Name'] =df_result['Column_Name'].apply(format_column_name)

    #Sauvegarder le résultat sous format csv
    #df_result.to_csv(output+".csv")
    return df_result


def get_csv_files_for_null_columns(input,output):

    df = pd.read_csv(input, header=0,low_memory=False)
    df = delete_empty_columns(df)
    serie = df.isnull().sum()

    df_result = pd.DataFrame({'Column_Name':serie.index, 'Number_of_empty_values':serie.values})

    # Sauvegarder le résultat sous format csv
    #df_result.to_csv(output+".csv")

    return df_result



def get_csv_merge_file(input, csv_output):

    output_rate = csv_output + "_rate"
    df_rate = get_csv_files_for_null_columns_rate(input,output_rate)

    output_total = csv_output + "_total"
    df_total = get_csv_files_for_null_columns(input,output_total)

    result = pd.concat([df_rate, df_total], axis=1, join="inner")
    result.to_csv(csv_output+".csv")

    return df_rate, df_total

def get_plot_for_null_columns_rate(df, fig_name):

    df = df[df.Rate_of_empty_values != 0]

    if(len(df) > 0):
        df.plot(x ='Column_Name', y='Rate_of_empty_values', kind = 'barh', stacked=False, width=0.7)

        ax = plt.gca()
        for index, value in enumerate(df.Rate_of_empty_values):
            plt.text(value + 0.5, index - 0.2, str(value)+"%")

        m = 2 # inch margin
        s = 20/plt.gcf().dpi*len(df)+2*m
        plt.gcf().set_size_inches(12, s)


        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend(loc='lower right')

        plt.xlabel("Rate_of_empty_values (%)", size = 12)
        plt.ylabel("Column_Name", size = 12)

        plt.title(fig_name, plt.tight_layout())
        plt.savefig(fig_name+".png")
        plt.show()

def get_plot_for_null_columns_total(df, fig_name):

    df = df[df.Number_of_empty_values != 0]
    if(len(df) > 0):
        df.plot(x ='Column_Name', y='Number_of_empty_values', kind = 'barh', stacked=False)

        ax = plt.gca()
        for index, value in enumerate(df.Number_of_empty_values):
            plt.text(value + 0.5, index - 0.2, str(value))

        m = 2 # inch margin
        s = 20/plt.gcf().dpi*len(df)+2*m
        plt.gcf().set_size_inches(12, s)


        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend(loc='lower right')


        plt.xlabel("Number_of_empty_values", size = 12)
        plt.ylabel("Column_Name", size = 12)

        plt.title(fig_name, plt.tight_layout())
        plt.savefig(fig_name+".png")
        plt.show()


"""


df_rate_business, df_total_business = get_csv_merge_file("../data/csv/business.csv", "../business/business_null_columns")

get_plot_for_null_columns_rate(df_rate_business, "../business/business_rate_empty_values")
get_plot_for_null_columns_total(df_total_business, "../business/business_number_empty_values")



df_rate_user, df_total_user = get_csv_merge_file("../data/csv/user.csv", "../user/user_null_columns")

get_plot_for_null_columns_rate(df_rate_user, "../user/user_rate_empty_values")
get_plot_for_null_columns_total(df_total_user, "../user/user_number_empty_values")


df_rate_review, df_total_review = get_csv_merge_file("../data/csv/review.csv", "./review/rereview_null_columns")

get_plot_for_null_columns_rate(df_rate_review, "../review/review_rate_empty_values")
get_plot_for_null_columns_total(df_total_review, "../review/review_number_empty_values")

df_rate_tip, df_total_tip = get_csv_merge_file("../data/csv/tip.csv", "./tip/tip_null_columns")

get_plot_for_null_columns_rate(df_rate_tip, "../tip/tip_rate_empty_values")
get_plot_for_null_columns_total(df_total_tip, "../tip/tip_number_empty_values")

df_rate_checkin, df_total_checkin = get_csv_merge_file("../data/csv/checkin.csv", "../checkin/checkin_null_columns")

get_plot_for_null_columns_rate(df_rate_checkin, "../checkin/checkin_rate_empty_values")
get_plot_for_null_columns_total(df_total_checkin, "../checkin/checkin_number_empty_values")

"""

df_rate_restaurants, df_total_restaurants = get_csv_merge_file("../data/csv/tip.csv", "./tip/tip_null_columns")

get_plot_for_null_columns_rate(df_rate_restaurants, "./tip/tip_rate_empty_values")
get_plot_for_null_columns_total(df_total_restaurants, "./tip/tip_number_empty_values")

#get_dataSet_initial_state("restaurants","review","user","tip","checkin")





