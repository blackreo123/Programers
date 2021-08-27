dict_column_name = {
        "通番": "serial_no",
        "社員ID": "employee_id",
        "Seq": "seq",
        "使用日": "use_date",
        # "勘定科目Key": "#N/A",
        "申請金額": "app_amount",
        "目的": "purpose",
        "内訳": "detail",
        "同席者": "company",
        "領収書イメージ": "receipt_image",
        "Workflow No": "workflow_no",
        "決裁ステータス": "approval_status",
        "支払日": "payment_date",
        "登録者ID": "create_user_id",
        "登録日時": "create_timestamp",
        "更新者ID": "update_user_id",
        "更新日時": "update_timestamp"
    }

data = {'使用日': '2021-08-15', '申請金額': 10000, '目的': '業務能力向上', '内訳': 'アイスクリームを食べたㅇㄴㅁㅇㄴㅁ', '同席者': '高潔', '領収書イメージ': 10000}

scolumn = ""
lst_value = []

for index, (key, value) in enumerate(data.items()):
    lst_value.append(str(value))
    if index < len(data) - 1:
        scolumn = scolumn + dict_column_name[key] + "=" + str(value) +","

    else:
        scolumn = scolumn + dict_column_name[key] + "=" + str(value)

print(scolumn)
    