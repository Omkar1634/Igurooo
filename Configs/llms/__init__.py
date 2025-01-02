from ._grog import GroqNode


class AgentFactory:
    """
    A factory class that creates instances of the GroqNode class.
    """

    
    @staticmethod
    def build(provider, **llm_config):
        """
        Create an instance of the GroqNode class.

        Returns:
            GroqNode: An instance of the GroqNode class.
        """
        try:
            match provider:
                case 'grog':
                    return GroqNode(**llm_config)
                case _:
                    raise ValueError(f"Unknown provider: {provider}")
        except Exception as e:
            raise e
            
    