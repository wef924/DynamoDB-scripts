table = self.dynamodb.Table('ProgramProject-beta')
resp = table.scan()
data = resp['Items']
for item in data:
    if item['program_project_key'].startswith('program#'):
        string = item['program_project_key']
    else:
        string = f"project#{item['program_id']}#{item['project_id']}"

    table.update_item(
        Key={'program_id': item['program_id'], 'program_project_key': item['program_project_key']},
        UpdateExpression='SET business_entity_id = :val1, business_entity_sort = :val2',
        ExpressionAttributeValues={
            ':val1': '9378eeb7-25c5-4b5a-8ee8-cd3ae678e38f',
            ':val2': string
        }
    )
return []