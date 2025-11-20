class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_map = {}
        recipe_map = {}
        n = len(recipes)
        count = 0
        for recipe in recipes:
            recipe_map[recipe] = count
            count+=1
        for supply in supplies:
            supply_map[supply] = 1

        ans = []

        visited = [0]*n
        for j in range(n):
            for i in range(len(ingredients)):
                if visited[i] != 0:
                    continue
                ad = 0
                for ing in ingredients[i]:
                    not_in_recipe = ing not in recipe_map
                    not_in_supply = ing not in supply_map

                    if not_in_recipe and not_in_supply:
                        visited[i] = 1
                    if not_in_supply==True:
                        ad = 1

                # print('not_in_recipe: ',not_in_recipe, ' not_in_supply: ',not_in_supply)
                if ad == 0:
                    supply_map[recipes[i]] = 1
                    ans.append(recipes[i])
                    visited[i] = 2

                # print(visited)

        return ans