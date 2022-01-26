from pycountry_convert import convert_countries
import plotly.express as px
import plotly.graph_objects as go


ccodes=['GT','TH','NO','BG','MC','IL','RO','IN','TR','DZ','GB',
'DO','SG','VN','SE','CO','LB','PT','AR','QA','EG','ES','CH',
'ID','MT','TW','MA','HU','OM','PY','BO','KW','LU','BR','IT','AT',
'SV','JP','PE','FI','IE','CA','BE','LI','IS','FR','BH','AD','MY','UY','LT','HN','TN','AU','ZA','PA',
'AE','NL','JO','CY','NI','CR','EC','MX','CZ','DE','GR','EE','PS','SK','PH','DK','US','LV','HK','PL','CL','NZ','SA']

inertias=[205095.20802699, 105504.27956194,  74670.76709451,  54333.03278889,
        45802.00107996,  38246.03515776,  33257.91823737,  29427.83211802,
        26711.07443283,  24167.70679879,  22234.10410585,  20634.62204422,
        19280.70855107,  18033.60086862,  16868.84642415,  15909.96231278,
        15008.49749629,  14262.5250447 ,  13511.3637936 ,  12910.49194498,
        12243.6450914 ,  11726.42085936,  11239.57289288,  10793.46380191]
max_cluster_count=24

def getCountryName(val):
    return convert_countries.country_alpha2_to_country_name(val).capitalize()

def getCountryCode(val):
    return convert_countries.country_name_to_country_alpha2(val.lower())

def getWorldFigure(cdata,col,country_list):
    cdata=    cdata[cdata.country_code.isin(country_list)]
    fig = go.Figure()
    fig.add_trace(go.Choropleth(locations = cdata['country_names'],z=cdata[col],
        locationmode='country names',text = 'country_names',colorscale = 'algae',autocolorscale=False,
        reversescale=True,marker_line_color='darkgray',marker_line_width=0.5,colorbar_tickprefix = '',
                                colorbar_title = col.replace('avg_','').capitalize(),))
    fig.update_layout(
        title_text='Average '+col.replace('avg_','').capitalize()+' across the world',
        geo=dict(
            showframe=True,
            showcoastlines=False,
            projection_type='equirectangular'
        ))
    return fig


def generateTracksDetailsPerCountry(data,country_codes,save=False,name=None):
    out={'country_code':country_codes,'num_tracks':[],'avg_acousticness': [],
         'avg_danceability': [],'avg_energy': [],'avg_instrumentalness': [],
         'avg_liveness': [],'avg_loudness': [],'avg_popularity': [],
         'avg_speechiness': [],'avg_tempo': [],'avg_valence': []}
    for country in tqdm(country_codes):
        out['num_tracks'].append(data[data.available_markets.str.contains(country)].shape[0])
        for col in ['acousticness', 'danceability', 'energy',
                   'instrumentalness', 'liveness', 'loudness', 
                   'popularity', 'speechiness', 'tempo', 'valence']:
            out['avg_'+col].append(data[data.available_markets.str.contains(country)][col].mean())
    if not save:
        return pd.DataFrame(out)
    else:
        if name==None:
            pd.DataFrame(out).to_csv('cdata.csv',index=None)
        else:
            pd.DataFrame(out).to_csv(name+'.csv',index=None)

