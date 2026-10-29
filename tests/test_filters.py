from apex_esp.core.models.player import Bone, PlayerSnapshot, Vec3
from apex_esp.core.models.world import LocalView
from apex_esp.features.esp.filters import keep_player


def _mk(team: int, x: float, hp: int = 100) -> PlayerSnapshot:
    return PlayerSnapshot(
        entity_id=1, name="t", team=team, health=hp, shield=0,
        origin=Vec3(x, 0, 0), bones=(Bone("head", Vec3(x, 0, 1.7)),),
    )


def test_enemy_in_range_kept():
    view = LocalView(Vec3(0, 0, 0), 0, 0, 90)
    assert keep_player(_mk(2, 50), view, local_team=1, max_m=400)


def test_teammate_filtered():
    view = LocalView(Vec3(0, 0, 0), 0, 0, 90)
    assert not keep_player(_mk(1, 50), view, local_team=1, max_m=400)


def test_dead_filtered():
    view = LocalView(Vec3(0, 0, 0), 0, 0, 90)
    assert not keep_player(_mk(2, 50, hp=0), view, local_team=1, max_m=400)