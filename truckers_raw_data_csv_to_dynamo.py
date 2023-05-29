import boto3
dynamodb = boto3.client('dynamodb')
# Change days_count if you change the number of days in your csv file
days_count = 7
with open('truckers_raw_data.csv', 'r') as file:
    body = file.read()
    splitted_body = body.split("\n")
    ignore_first = True
    for line in splitted_body:
        if ignore_first:
            ignore_first = False
            continue
        a = line.split(",")
        item = {
            'id': {'S': a[0]},
            'location': {'S': a[1]},
            'february': {
            'M': {}
        }   
            }
        for i in range(1, days_count+1):
            item['february']['M'][f"0{i}"] = {'M': {'status': {'S': a[i+1]}}}
        print(item)
        dynamodb.put_item(TableName="truckers", Item=item)