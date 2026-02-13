import requests
import json


class ScaleDownClient:
    def __init__(self, api_key):
        self.url = "https://api.scaledown.xyz/compress/raw/"
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def compress(self, context, prompt):
        payload = {
            "context": context,
            "prompt": prompt,
            "scaledown": {
                "rate": "auto"
            }
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            data=json.dumps(payload)
        )

        result = response.json()

        if result.get("successful"):
            return result["compressed_prompt"]
        else:
            raise Exception("ScaleDown compression failed")
