# # Getting Compatible Libraries
FROM public.ecr.aws/lambda/python:3.8

# # Installing Dependencies
RUN pip3 install awslambdaric==1.0.0
RUN pip3 install boto3==1.17.79

# # Copying the Python Script
COPY ./stop_instance.py /var/task

# # Running the Python Script
CMD ["start_instance.handler"]

