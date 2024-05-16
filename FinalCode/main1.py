from mouse_tracking import track_user_path
from generate_screenshot import generate_user_path
from similarity import compute_similarity_mouse_tracking_based
from DB_utilities import insert_mouse_similarity


track_user_path()
generate_user_path()
result = compute_similarity_mouse_tracking_based()
insert_mouse_similarity(result)