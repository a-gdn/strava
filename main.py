from utils.helper_functions import get_config, get_df_from_db

from data_extract.extract import ExtractStravaData
from data_transform.activities import CreateActivities
from data_transform.summary import SummarizeActivities
from data_plot.summary import PlotSummary

def main() -> None:
    ExtractStravaData().update_strava_activities_db()

    cfg = get_config()
    strava_activities_df = get_df_from_db(cfg.db.extract.folder_path, cfg.db.extract.activities_file_name)
    CreateActivities().create_activities_db(strava_activities_df)

    activities_df = get_df_from_db(cfg.db.transform.folder_path, cfg.db.transform.activities_file_name)
    SummarizeActivities().create_summary_db(activities_df)

    activities_df = get_df_from_db(cfg.db.transform.folder_path, cfg.db.transform.summary_file_name)

    # print('hello')

if __name__ == "__main__":
    main()