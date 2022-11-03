from fastapi import APIRouter

from .views import get_i_number, get_f_number


random_app = APIRouter(prefix="/random")

random_app.add_api_route("/int", get_i_number, methods=["POST"])
random_app.add_api_route("/float", get_f_number, methods=["POST"])
