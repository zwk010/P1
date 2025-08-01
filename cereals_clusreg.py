import project_1v2_0

all_exports_capita = project_1v2_0.load_pop_data()

resource = all_exports_capita[0]
minfilter = 10
maxfilter = 400
yscalar = 1
resource = project_1v2_0.remove_outliers(resource, "dollar_per_capita", minfilter, maxfilter)
clusterdata = project_1v2_0.perform_kmeans_clustering(resource, ['dollar_per_capita', 'HDI_value'], 4, yscalar)
clusterdata = project_1v2_0.country_code_to_names(clusterdata)
clusterdata.to_csv('data/clustering_results/cereals.csv', index=False)

project_1v2_0.combined_regression_clustering_linear(
    [minfilter, maxfilter, yscalar],
    'Cereals', full_clustered_df=clusterdata,
    cluster_filtered_dfs=[
        (clusterdata, [2], 'C1'),
        (clusterdata, [], 'C2')
    ],
    xcol='dollar_per_capita',
    ycol='HDI_value'
)