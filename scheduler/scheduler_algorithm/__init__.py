from gym.envs.registration import register

register(
    id="scheduler_algorithm/Scheduler-v0",
    entry_point="scheduler_algorithm.envs:SchedulerEnvironment",
)
