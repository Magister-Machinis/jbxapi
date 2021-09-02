import argparse
import json
import jbxapi

parsed = argparse.ArgumentParser()
parsed.add_argument("--apikey",type=str)
parsed.add_argument("--filepath",type=str)
parsed.add_argument("--time",type=str)
parsed.add_argument("--comment",type=str)
parsed.add_argument("--tags",type=str)
parsed = parsed.parse_args()

jbx = jbxapi.JoeSandbox(apikey=parsed.apikey)
with open(parsed.filepath, 'rb') as file:
 print(json.dumps(jbx.submit_sample(file, _extra_params={"comments":parsed.comment, "analysis-time":parsed.time, "tags[]":parsed.tags.split(',')})))
