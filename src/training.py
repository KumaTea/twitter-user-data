import pathlib
from fastai.tabular.all import *


header = ['tid', 'yr', 'mo', 'dt', 'wk', 'dow', 'doy', 'time', 'last', 'nxt', 'tlen', 'media', 'src', 'isq', 'sen', 'lang',
          'snlen', 'prot', 'foing', 'foer', 'crd', 'favcnt', 'tcnt',
          'lcnt']
cont = ['tid', 'yr', 'mo', 'dt', 'wk', 'dow', 'doy', 'time', 'last', 'nxt', 'tlen',
        'snlen', 'foing', 'foer', 'crd', 'favcnt', 'tcnt']
cat = ['media', 'src', 'isq', 'sen', 'lang',
       'prot']


df = pd.read_csv('../data/combined.csv')
path = pathlib.Path('.')

dls = TabularDataLoaders.from_df(
    df, path=path,
    y_names='lcnt', y_block=RegressionBlock,
    cat_names=cat, cont_names=cont,
    procs=[Categorify, FillMissing, Normalize],
    bs=1024
)

learn = tabular_learner(dls, splitter=RandomSplitter(valid_pct=0.1, seed=42), metrics=accuracy)
print(learn.metrics)

learn.fit(5)
