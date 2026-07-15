from fastapi import APIRouter

from backend.app.providers.provider_factory import ProviderFactory

router = APIRouter(
    prefix="/api/v1/provider",
    tags=["Provider"],
)


@router.get("/status")
def status():

    provider = ProviderFactory.get_provider()

    return {
        "provider": provider.provider_name(),
    }
