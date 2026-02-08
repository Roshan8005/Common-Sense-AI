# Special Sense AI: Causal Reasoning Framework
# Developed by: Roshan Kumar Sah (BMIT, RGUHS)

class SpecialSenseAI:
    def __init__(self):
        # The 'Chitta' (Memory Store)
        self.common_sense_knowledge = {
            'ball_in_street': {
                'prediction': '⚽ Child may follow the ball!',
                'action': '🛑 STOP VEHICLE IMMEDIATELY',
                'urgency': 'High'
            },
            'child_crying': {
                'prediction': '🚼 Potential hunger, pain, or fear.',
                'action': '🤝 Offer comfort and assess needs.',
                'urgency': 'Medium'
            },
            'ice_on_road': {
                'prediction': '🧊 Friction is reduced; road is slippery.',
                'action': '⚠️ Reduce speed and increase distance.',
                'urgency': 'High'
            }
        }

    def buddhi_gate(self, stimulus):
        """The Discernment Layer (Buddhi)"""
        print(f"Perceiving (Manas): {stimulus}")
        
        # Check if the stimulus exists in the logic database
        if stimulus in self.common_sense_knowledge:
            logic = self.common_sense_knowledge[stimulus]
            return f"Reasoning: {logic['prediction']}\nRecommended Action: {logic['action']}"
        else:
            return "Reasoning: Context unknown. Reverting to safe-state observation."

# --- Testing the Architecture ---
ai = SpecialSenseAI()

# Test Case 1: Road Safety
print(ai.buddhi_gate('ball_in_street'))

# Test Case 2: Human Care
print("\n" + ai.buddhi_gate('child_crying'))
