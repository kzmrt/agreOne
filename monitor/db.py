import logging
import mysql.connector
from mysql.connector import errorcode
import configparser

ini = configparser.ConfigParser()
ini.read('./config.ini', 'UTF-8')

logger = logging.getLogger('development')

## 接続先DB情報
config = {
    'user': ini['db_info']['user'], #'testUser',
    'password': ini['db_info']['password'], #'testtest',
    'host': ini['db_info']['host'], #'localhost',
    'database': ini['db_info']['database'], #'testData',
    'raise_on_warnings': True
}

sql_get_greenhouse = ("SELECT `greenhouse`.`id`, `greenhouse`.`location_id`, `greenhouse`.`data_datetime`, `greenhouse`.`temp_out`, `greenhouse`.`temp_in`, `greenhouse`.`temp_set`, `greenhouse`.`temp_vent`, `greenhouse`.`temp_heat`, `greenhouse`.`temp_soil`, `greenhouse`.`rh_out`, `greenhouse`.`rh_in`, `greenhouse`.`rain`, `greenhouse`.`irradiance`, `greenhouse`.`co2_conc`, `greenhouse`.`co2_set`, `greenhouse`.`net_photos`, `greenhouse`.`transpiration`, `greenhouse`.`head_load`, `greenhouse`.`head_load_pu`, `greenhouse`.`control_mode`, `greenhouse`.`night_cool_mode`, `greenhouse`.`window_opening`, `greenhouse`.`window_kp`, `greenhouse`.`curtain_mode`, `greenhouse`.`hp_heat`, `greenhouse`.`hp_cool`, `greenhouse`.`hf`, `greenhouse`.`mist`, `greenhouse`.`exhaust_fun`, `greenhouse`.`co2`, `greenhouse`.`co2_sec`, `greenhouse`.`dehumidify`, `greenhouse`.`fan_mode`, `greenhouse`.`fan_speed`, `greenhouse`.`shutter`, `greenhouse`.`fan2_mode`, `greenhouse`.`fan2_speed`, `greenhouse`.`shutter2`, `greenhouse`.`created_at`, `greenhouse`.`updated_at`, `location`.`id`, `location`.`name`, `location`.`memo`, `location`.`author_id`, `location`.`created_at`, `location`.`updated_at` "
                        "FROM `greenhouse` INNER JOIN `location` ON (`greenhouse`.`location_id` = `location`.`id`) "
                        "WHERE (`greenhouse`.`data_datetime` "
                        "BETWEEN %s AND %s "
                        "AND `greenhouse`.`location_id` = %s);")

class getDbRecord:

    ## Greenhouseレコード取得
    def getGreenhouseRecord(pk, start_datetime, end_datetime):

        try:
            db = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error("ユーザ名またはパスワードが違います。")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logger.error("存在しないデータベースです。")
            else:
                logger.error(err)
        else:
            logger.info('== Start DBレコード取得 ==')
            cursor = db.cursor()

            add_params = []
            add_params.append(start_datetime)
            add_params.append(end_datetime)
            add_params.append(pk)

            cursor.execute(sql_get_greenhouse, add_params)
            rows = cursor.fetchall()
            logger.info("== End DBレコード取得 ==")
            logger.info("データサイズ：" + str(len(rows)))
            return rows

            # DB後処理
            cursor.close()
            db.close()