from flask import Flask, render_template, request
import logging
import sys
from llama_index.prompts import PromptTemplate
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
import os
import time
import json

os.environ["OPENAI_API_KEY"] = "sk-"

app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Configurando as opções de exibição do pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv("./data/df_100 1.csv")

new_prompt = PromptTemplate(
    """\
You are working with a pandas dataframe in Python.
The name of the dataframe is `df`.
This is the result of `print(df.head())`:
{df_str}
Full report response follows this structure:
    "timestamp": "11-01-2023",
    "Time": "00:04:00",
    "day_period": "Wednesday",
    "day_of_week": "11 January",
    "month_day": "11",
    "month": "January",
    "dew_point": "-5.621632",
    "process_dew_point": "Don't Criticize",
    "contactor_pressure": "161.305446",
    "process_contactor_pressure": "Low",
    "natural_gas_moisture": "2.71",
    "process_natural_gas_moisture": "Normal",
    "contactor_temperature": "42.6",
    "process_contactor_temperature": "Low",
    "glycol_moisture": "0.67",
    "process_glycol_moisture": "Efficient",
    "water_inlet_temperature":"34.56",
    "process_water_inlet_temperature": "Normal",
    "glycol_inlet_temperature": "52.67",
    "process_glycol_inlet_temperature": "Low",
    "out_glycol_temperature": "40.75",
    "process_out_glycol_temperature":"Good",
    "temperature": "183.626183",
    "process_temperature": "Keep",
    "out_water_temperature": "58.355965",
    "process_out_water_temperature": "Bad",
    "stripping_gas": "107.583807",
    "process_stripping_gas": "Normal",
    "pressure": "33.85637",
    "process_pressure": "Normal Pressure",
    "dry_glycol": "0.79",
    "process_dry_glycol": "Not Worrying",
    "glycol_flow": "1.925554",
    "process_glycol_flow": "Ok",
Follow these instructions:
1. "In the response for individual columns, the response format should be as follows, using the column 'Glycol Flow' as an example: 'Glycol Flow': '1.728669'."
{instruction_str}
Query: {query_str}

Expression: """
)

query_engine = PandasQueryEngine(df=df, synthesize_response=True)
query_engine.update_prompts({"pandas_prompt": new_prompt})

#"Give me the information you can get on the date '09-01-2023' ?"
#Process Natural Gas Moisture date 11-10-2023
#Value Glycol Flow 25-12-2022

def index():
    return render_template('index.html')

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')  # Use get() para evitar KeyError
        response = query_engine.query(user_input)
        formatted_data = response.metadata["raw_pandas_output"]
        json_string = json.dumps(formatted_data)
        resposta_formatada = json_string.replace("{", "").replace("}", "").replace(", ", ",\n")
        return render_template('index.html', user_input=user_input, resposta_formatada=resposta_formatada)
    if request.method == 'GET':
        return render_template('index.html', user_input='Sua pergunta', resposta_formatada='Faça pergunta ao seu DOCUMENTO')

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

