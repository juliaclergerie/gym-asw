from gym.envs.registration import register

register(
    id='asw-v0',
    entry_point='gym_asw.envs:AswEnv',
)
register(
    id='asw-extrahard-v0',
    entry_point='gym_asw.envs:AswExtraHardEnv',
)

