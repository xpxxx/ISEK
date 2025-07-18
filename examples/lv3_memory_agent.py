from isek.agent.isek_agent import IsekAgent
from isek.models.openai import OpenAIModel
from isek.memory.memory import Memory
from isek.models.base import SimpleMessage
import dotenv
dotenv.load_dotenv()

# Create memory instance
memory = Memory(debug_mode=True)

# Create agent with memory
agent = IsekAgent(
    name="Memory Agent",
    model=OpenAIModel(model_id="gpt-4o-mini"),
    memory=memory,
    description="A helpful assistant with memory",
    instructions=["Be polite", "Provide accurate information", "Remember previous conversations"],
    success_criteria="User gets a helpful response that takes into account previous interactions",
    debug_mode=True
)

# # Test conversation with memory

agent.print_response("Hello! My name is Alice.", user_id="alice", session_id="session1")    
agent.print_response("What's my name?", user_id="alice", session_id="session1")
agent.print_response("Tell me about our previous conversations.", user_id="alice", session_id="session1")

# Show memory contents
print("\n=== Memory Contents ===")
print(f"User memories: {len(memory.get_user_memories('alice'))}")
for i, memory_item in enumerate(memory.get_user_memories('alice')):
    print(f"Memory {i+1}: {memory_item.memory}")

print(f"\nSession runs: {len(memory.get_runs('session1'))}")
for i, run in enumerate(memory.get_runs('session1')):
    print(f"Run {i+1}: {run}")
