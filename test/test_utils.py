from src.utils import convert_csv_to_dataframe
import pandas as pd


def test_returns_dataframe_in_expected_format_for_file_of_bought_parts():
    input_path = 'example_csv/24-201-107.csv'
    result = convert_csv_to_dataframe(input_path)
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns.values) == ['Part No', 'Description', 'Dwg Ref', 'Qty', 'Source', 'Destination']

    pd.testing.assert_frame_equal(result, result[result['Source'] == 'B'])

def test_sums_quanitities_of_nested_drawings():
    input_path = 'example_csv/24-201-101.csv'
    result = convert_csv_to_dataframe(input_path)

    # print(result[result['Description'] == 'Bolt'])
    assert False