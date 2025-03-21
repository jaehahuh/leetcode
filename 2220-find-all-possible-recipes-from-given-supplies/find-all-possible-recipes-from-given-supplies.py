class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {sup:True for sup in supplies} # Supplies can always be made, so set to True
        recipe_index = {r:i for i,r in enumerate(recipes)}

        def dfs(recipe):
            # If the recipe has already been computed, return its value
            if recipe in can_cook:
                return can_cook[recipe]

            # If the recipe is not in the list, it cannot be made
            if recipe not in recipe_index:
                return False

            can_cook[recipe] = False  # Mark the current recipe as being visited (to prevent circular dependency)

            for nei in ingredients[recipe_index[recipe]]:
                # If any ingredient cannot be made, the current recipe cannot be made
                if not dfs(nei):
                    return False
            
            # If all ingredients can be made, the current recipe can also be made
            can_cook[recipe] = True
            return can_cook[recipe]
        
        return [recipe for recipe in recipes if dfs(recipe)]