    LLMConfig,
    default_llm = LLMConfig(
        draft_editor=LLMConfig()  # just to prevent eval errors
    )
            remote_runtime_api_url=os.environ.get('SANDBOX_REMOTE_RUNTIME_API_URL'),
    config.set_llm_config(default_llm)