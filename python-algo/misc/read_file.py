import json


def parse(rpath: str, wpath: str, sql: str):
    txt = ''
    with open(rpath) as f:
        for line in f:
            values = line.split(',')
            # values[1] = values[1][:-1]
            txt += sql.format(*values)
            txt += '\n'
    wf = open(wpath, 'w')
    res = wf.write(txt)
    wf.close()
    print(res)
    print(txt)


def parse_json_file(rpath: str):
    store = {}
    with open(rpath) as f:
        raw = json.load(f)
        for ele in raw:
            store[ele['name']] = {"name": ele['name'], "id": ele['id']}
    return store


if __name__ == '__main__':
    # sql = """INSERT INTO compensation_config_order (merchant_id, merchant_name, app_id, shop_merchant_id, shop_app_id, advance_merchant_id, advance_app_id, advance_hz_uid, advance_zfb_uid, advance_wx_uid, advance_uid_type, status, compensation_sence, remark, creator, last_operator, create_time, update_time) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', {10}, '{11}', '{12}', '{13}', '{14}', '{15}', now(), now());"""
    # sql = """update refund_cf_fsm_record set status='C' where biz_trans_no='{0}' and sharding_key='{1}' limit 1;"""
    # sql = """update refund_detail set split_status='SUCCESS' where id='{0}' and sharding_key='{1}' limit 1;"""
    # sql = """INSERT INTO fc_config_order (merchant_id, merchant_name, out_app_id, payer_app_id, payee_app_id, payee_uid, payee_uid_type, fc_sence_code, fc_sence_name, fc_type, biz_sence, compensation_sence, remark, status, creator, last_operator, create_time, update_time) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '', now(), now());"""
    # parse('/Users/zhangjian/Downloads/fc_conf.csv', '/Users/zhangjian/Downloads/fc.sql', sql)
    # sql = """update tp_refund_limit set out_refund_no_to_refund_amount='{{}}', in_avail_amount={2}, channel_avail_amount={4} where origin_trade_no='{0}' and version = 2 and sharding_key='{1}' limit 1;"""
    # parse('/Users/bytedance/Downloads/refund_limit.csv',
    #       '/Users/bytedance/Downloads/refund_limit.sql', sql)
    filename = 'caijing.doupay.trade_advance'
    lret = parse_json_file('/Users/bytedance/Downloads/' + filename + '_规则导出.json')
    rret = parse_json_file('/Users/bytedance/Downloads/' + filename + '_规则导出2.json')
    diff = ''
    for k, v in lret.items():
        if k not in rret:
            diff += lret[k].__str__()
            diff += '\n'

    wf = open('/Users/bytedance/Downloads/'+ filename + '_alert_diff.json', 'w')
    res = wf.write(diff)
    wf.close()
