from requests import get
from joblib.memory import Memory
import pandas as pd
import matplotlib.pyplot as plt

cache = Memory("cache", verbose=0).cache
get = cache(get)


@cache
def get_data():
    params = dict(
        type="query",
        query='type:Article text:"ai safety"',
        size=str(5_000),
        token="d146723d71f526e2562d2fc403b0f3d4",
    )
    response = get("https://kg.diffbot.com/kg/v3/dql", params=params)
    # print(response.text[:1000])
    data = response.json()["data"]
    data = [d["entity"] for d in data]
    df = pd.DataFrame(data)
    df["date"] = df["date"].apply(lambda x: x["str"][1:] if not pd.isna(x) else None)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df[["date", "sentiment"]].dropna()
    rdf = df

    df = rdf.copy()
    # aggregate counts and mean sentiment by day
    df = df[df["date"] >= "2010-01-01"]
    df = (
        df.groupby("date")
        .agg({"sentiment": ["count", "mean"]})
        .droplevel(0, axis=1)
        .rename(columns={"count": "count", "mean": "sentiment"})
    )
    # fill missing dates with 0 counts and NaN sentiment

    df = df.reindex(
        pd.date_range(df.index.min(), df.index.max(), freq="D"), fill_value=0
    )
    df.columns = ["count", "sentiment"]
    df = df.resample("M").sum()
    return df
    # plot counts and sentiment
    # df["count"].plot()
    # df["sentiment"].plot(secondary_y=True)
    # plt.show()
    # by month
    # df["count"].resample("M").sum().plot()
    # plt.show()
    # df["sentiment"].resample("M").mean().plot()
    # plt.show()
