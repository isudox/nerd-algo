def parse0(rpath: str, wpath: str, sql: str):
    txt = ''
    with open(rpath) as f:
        for line in f:
            values = line.split(',')
            values[1] = values[1][:-1]
            txt += sql.format(*values)
            txt += '\n'
    wf = open(wpath, 'w')
    res = wf.write(txt)
    wf.close()
    print(res)
    print(txt)


if __name__ == '__main__':
    # sql = """INSERT INTO compensation_config_order (merchant_id, merchant_name, app_id, shop_merchant_id, shop_app_id, advance_merchant_id, advance_app_id, advance_hz_uid, advance_zfb_uid, advance_wx_uid, advance_uid_type, status, compensation_sence, remark, creator, last_operator, create_time, update_time) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', {10}, '{11}', '{12}', '{13}', '{14}', '{15}', now(), now());"""
    sql = """update refund_cf_fsm_record set status='C' where biz_trans_no='{0}' and sharding_key='{1}' limit 1;"""
    parse0('/Users/zhangjian/Downloads/fix.csv', '/Users/zhangjian/Downloads/fix.sql', sql)
    # sql = """INSERT INTO fc_config_order (merchant_id, merchant_name, out_app_id, payer_app_id, payee_app_id, payee_uid, payee_uid_type, fc_sence_code, fc_sence_name, fc_type, biz_sence, compensation_sence, remark, status, creator, last_operator, create_time, update_time) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '', now(), now());"""
    # parse0('/Users/zhangjian/Downloads/fc_conf.csv', '/Users/zhangjian/Downloads/fc.sql', sql)
