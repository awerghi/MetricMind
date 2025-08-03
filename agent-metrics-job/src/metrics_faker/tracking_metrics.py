from prometheus_client import Counter

generated_events = lambda registry : Counter("fake_metrics_events_number",
                                             "the number of fake metrics generated in order to be sent to kafka",
                                              registry=registry)
fake_metrics_published_success = lambda registry : Counter("metrics_published_success",
                                                           "the number of metrics that has been published with success to kafka",
                                                           registry=registry)
fake_metrics_published_error = lambda registry : Counter("metrics_published_error",
                                                         "the number of metrics that has not been published to kafka",
                                                          registry=registry)