import gymnasium as gym

_ADAM_LITE_VELOCITY_KWARGS = {
    "env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotEnvCfg",
    "play_env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotPlayEnvCfg",
    "rsl_rl_cfg_entry_point": f"unitree_rl_lab.tasks.locomotion.agents.rsl_rl_ppo_cfg:BasePPORunnerCfg",
}

gym.register(
    id="Unitree-Adam-Lite-Velocity",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs=_ADAM_LITE_VELOCITY_KWARGS,
)
# Historical id: same env as Adam Lite (URDF / cfg no longer use G1 USD).
gym.register(
    id="Unitree-G1-29dof-Velocity",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs=_ADAM_LITE_VELOCITY_KWARGS,
)
# Alias: ``UNITREE_ADAM_LITE_23DOF_CFG`` is the robot articulation cfg in code, not a gym id; users sometimes pass it as --task.
gym.register(
    id="UNITREE_ADAM_LITE_23DOF_CFG",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs=_ADAM_LITE_VELOCITY_KWARGS,
)
