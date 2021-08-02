import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int index1 = 0;
        int index2 = 0;
        HashMap<Integer, Integer> differences = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++){
            differences.put(nums[i], i);
        }
        
        for (int i=0; i < nums.length; i++){
            if(differences.containsKey(target-nums[i])){
                index1 = i;
                index2 = differences.get(target-nums[i]);
                if(index1 != index2){
                   return new int[] {index1, index2}; 
                }
            }
        }
        
        return new int[] {};
    }
}