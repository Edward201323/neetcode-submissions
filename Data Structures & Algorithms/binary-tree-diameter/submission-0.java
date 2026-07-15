/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        getDiameter(root);
        return maxDiameter;
    }

    public int getDiameter(TreeNode root){
        if(root == null){
            return 0;
        }

        int left = getDiameter(root.left);
        int right = getDiameter(root.right);

        int diameter = left + right;
        if(diameter > maxDiameter){
            maxDiameter = diameter;
        }

        if(left > right){
            return left + 1;
        } else {
            return right + 1;
        }

    }

}
