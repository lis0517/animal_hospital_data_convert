import csv
import os
import sys
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def csv_to_sql(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {input_file}")

        df = pd.read_csv(input_file, encoding='utf-8')  # UTF-8 인코딩 명시

        with open(output_file, 'w', encoding='utf-8') as sqlfile:
            for _, row in df.iterrows():
                business_name = str(row.get('사업장명', ''))
                address = str(row.get('소재지전체주소', ''))
                road_address = str(row.get('도로명전체주소', ''))
                phone = str(row.get('소재지전화', ''))
                lat = row.get('Latitude', 'NULL')
                lon = row.get('Longitude', 'NULL')

                if pd.isna(lat) or pd.isna(lon):
                    logging.warning(f"좌표 누락: {business_name}, {address}")
                    continue

                sql = f"('{business_name}', '{address}', '{road_address}', {lat}, {lon}, 'PET_HOSPITAL', '{phone}', NULL, false),\n"
                sqlfile.write(sql)

        logging.info(f"SQL 파일이 생성되었습니다: {output_file}")
    except Exception as e:
        logging.error(f"처리 중 오류 발생: {e}")
        raise

if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_csv = sys.argv[1]
        output_sql = sys.argv[2]

        logging.info(f"입력 CSV 파일: {input_csv}")
        logging.info(f"출력 SQL 파일: {output_sql}")

        csv_to_sql(input_csv, output_sql)
    else:
        print("CSV to SQL 변환을 위해서는: python script.py <입력_CSV_파일> <출력_SQL_파일>")