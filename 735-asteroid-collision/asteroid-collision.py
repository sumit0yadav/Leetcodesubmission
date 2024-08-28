class Solution:
    def asteroidCollision(self, l: List[int]) -> List[int]:
        st = []
        i = 0

        while i < len(l):
            if not st:
                st.append(l[i])
            else:
                # If both are of the same sign, just add to stack
                if st[-1] * l[i] > 0:
                    st.append(l[i])
                elif st[-1] > 0 and l[i] < 0:  # Potential collision
                    # Resolve the collision
                    while st and st[-1] > 0 and st[-1] <= abs(l[i]):
                        if st[-1] == -l[i]:
                            st.pop()  # Both values cancel out
                            break
                        else:
                            st.pop()  # Remove the positive value
                    else:
                        if not st or st[-1] < 0:
                            st.append(l[i])  # No more collisions or only negatives remain
                else:
                    st.append(l[i])  # If no collision, just append
            i += 1

        return st
        