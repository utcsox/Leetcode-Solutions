class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()

                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    asteroid = 0
                    break

                else:
                    asteroid = 0
                    break

            if asteroid:
                stack.append(asteroid)


        return stack
