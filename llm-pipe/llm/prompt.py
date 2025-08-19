import json
import logging

from langchain_mistralai import ChatMistralAI

from core.conf import settings
from db.utils.alerts_db_operations import push_alert_to_db
from models import CriticalMetricEvents


def build_prompt(prompt_operation,events,additional_prompt):
    return  f"{prompt_operation} {events} {additional_prompt}"

llm = ChatMistralAI(api_key="", model=settings.Model_Version)

def prompt_llm_with_retry(db,events,prompt_operation,additional_prompt,number_of_retries):
    prompt = build_prompt(prompt_operation,events,additional_prompt)
    structured_llm = llm.with_structured_output(CriticalMetricEvents)
    llm_response = structured_llm.invoke(prompt)
    llm_response_list = []
    if llm_response is not None:
        for metric in llm_response.response:
            llm_response_list.append(metric.model_dump())
        converted_events = [json.loads(event.value().decode('utf-8')) for event in events]
        llm_mixed_res = [{**d1, **d2} for d1, d2 in zip(llm_response_list, converted_events)]

        for llm_response in llm_mixed_res:
            push_alert_to_db(db,llm_response)

    elif number_of_retries > 0:
        prompt_llm_with_retry(db,events,prompt_operation,additional_prompt,number_of_retries-1)
    else :
        logging.error("cannot get response from llm after a fixed number of retries")