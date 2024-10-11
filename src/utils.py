import pandas as pd

def convert_csv_to_dataframe(filepath):
    df = pd.read_csv(filepath, index_col='Dwg Ref')
    print(df)
    # df = df.drop(columns=['Part No'])

    machined_parts = df[df['Source'] == 'M']
    bought_parts = df[df['Source'] == 'B']
    # print(bought_parts)
    if machined_parts.empty:
        return df
    part_nos = machined_parts['Dwg Ref'].to_list()


    for part in part_nos:
        quantity = machined_parts.loc[machined_parts['Dwg Ref'] == part, 'Qty'].iloc[0]
        subframe = convert_csv_to_dataframe(f'example_csv/{part}.csv')
        subframe['Qty'] = subframe['Qty'] * quantity
        # print(subframe, 'EXTRA\n\n')
        print(bought_parts)
        print(subframe)
        # on = ['Dwg Ref', 'Description', 'Source', 'Destination']
        # total_frame = pd.merge(bought_parts.drop(columns=['Qty']), subframe.drop(
        #     columns=['Qty']), how='outer')
        # bought_parts.set_index('Dwg Ref')
        # subframe.set_index('Dwg Ref')
        # total_frame['Qty'] = bought_parts['Qty'] + subframe['Qty']
        # print(total_frame, '<<<')

        # bought_parts = bought_parts + subframe

    # print(bought_parts)
    # aggregate_funcs = {'Part No': 'first', 'Description': 'first', 'Qty' : 'sum', 'Source': 'first', 'Destination': 'first'}
    # totalled_parts = bought_parts.groupby('Dwg Ref').sum(numeric_only=True)

    # print(totalled_parts)
    

        
