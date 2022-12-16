class MyQueue {
    ArrayList<Integer> queue;
    public MyQueue() {
        this.queue = new ArrayList<Integer>();
    }
    
    public void push(int x) {
        this.queue.add(x);
    }
    
    public int pop() {
        return this.queue.remove(0);
    }
    
    public int peek() {
        return this.queue.get(0);
    }
    
    public boolean empty() {
        if (this.queue.size() == 0){
            return true;
        }
        else{
            return false;
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
