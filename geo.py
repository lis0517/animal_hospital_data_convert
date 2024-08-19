import geokakao as gk
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_csv(input_file, output_file):
    try:
        logging.info(f"CSV 파일 읽기 시작: {input_file}")
        data = pd.read_csv(input_file, encoding='utf-8')
        logging.info(f"CSV 파일 읽기 완료. 행 수: {len(data)}")

        logging.info("좌표 추가 시작")
        gk.add_coordinates_to_dataframe(data, '소재지전체주소')
        logging.info("좌표 추가 완료")

        logging.info(f"결과 CSV 파일 저장 시작: {output_file}")
        data.to_csv(output_file, index=False, encoding='utf-8')
        logging.info("결과 CSV 파일 저장 완료")

    except Exception as e:
        logging.error(f"처리 중 오류 발생: {e}")
        raise

if __name__ == "__main__":
    input_file = 'fulldata_02_03_01_P.csv'
    output_file = 'output.csv'
    process_csv(input_file, output_file)