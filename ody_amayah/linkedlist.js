function Node(value){
    this.value = value;
    this.next = null;
}

function LinkedList() {
    this.head = null;

    this.removeFront = function() {
        if(!this.head){
            return this;
        }
        this.head = this.head.next;
        return this;
    }
}

LinkedList.prototype.addFront = function(value){
    var newNode = new Node(value);
    var oldHead =this.head;
    this.head =newNode;
    newNode.next =oldHead;
    return this;
}

var List = new LinkedList();
var node1 = new Node(1);
list.head = node1;

list.removeFront();
