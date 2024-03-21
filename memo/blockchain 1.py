import hashlib
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "0", 1465154705, "Genesis Block", self.calculate_hash("0"))

    def calculate_hash(self, block):
        """Calculate the hash of a block"""
        encoded_block = str(block.index) + str(block.previous_hash) + str(block.timestamp) + str(block.data)
        return hashlib.sha256(encoded_block.encode('utf-8')).hexdigest()

    def add_block(self, block):
        """Add a new block to the blockchain"""
        block.previous_hash = self.chain[-1].hash
        block.hash = self.calculate_hash(block)
        self.chain.append(block)

    def is_valid(self):
        """Check if the blockchain is valid"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != self.calculate_hash(current_block):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class User:
    def __init__(self, name):
        self.name = name
        self.key = ''.join(random.choices('0123456789abcdef', k=64))

    def get_key(self):
        return self.key

def generate_password(users):
    """Generate a password by combining the keys of all users"""
    keys = [user.get_key() for user in users]
    return hashlib.sha256(','.join(keys).encode('utf-8')).hexdigest()

# Create a new blockchain
blockchain = Blockchain()

# Create some users
users = [User("Alice"), User("Bob"), User("Charlie")]

# Add some blocks to the blockchain
blockchain.add_block(Block(1, blockchain.chain[-1].hash, 1465154706, "Transaction Data 1", ""))
blockchain.add_block(Block(2, blockchain.chain[-1].hash, 1465154707, "Transaction Data 2", ""))

# Check if the blockchain is valid
print(blockchain.is_valid())

# Generate the password
password = generate_password(users)
print("Password: " + password)
\
    >:.?://generate_password locked frozenset exit KeyError.
    \import hashlib
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "0", 1465154705, "Genesis Block", self.calculate_hash("0"))

    def calculate_hash(self, block):
        """Calculate the hash of a block"""
        encoded_block = str(block.index) + str(block.previous_hash) + str(block.timestamp) + str(block.data)
        return hashlib.sha256(encoded_block.encode('utf-8')).hexdigest()

    def add_block(self, block):
        """Add a new block to the blockchain"""
        block.previous_hash = self.chain[-1].hash
        block.hash = self.calculate_hash(block)
        self.chain.append(block)

    def is_valid(self):
        """Check if the blockchain is valid"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != self.calculate_hash(current_block):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

class User:
    def __init__(self, name):
        self.name = name
        self.key = ''.join(random.choices('0123456789abcdef', k=64))

    def get_key(self):
        return self.key

def generate_password(users):
    """Generate a password by combining the keys of all users"""
    keys = [user.get_key() for user in users]
    return hashlib.sha256(','.join(keys).encode('utf-8')).hexdigest()

# Create a new blockchain
blockchain = Blockchain()

# Create some users
users = [User("Alice"), User("Bob"), User("Charlie")]

# Add some blocks to the blockchain
blockchain.add_block(Block(1, blockchain.chain[-1].hash, 1465154706, "Transaction Data 1", ""))
blockchain.add_block(Block(2, blockchain.chain[-1].hash, 1465154707, "Transaction Data 2", ""))

# Check if the blockchain is valid
print(blockchain.is_valid())

# Generate the password
password = generate_password(users)
print("Password: " + password)
\n\n Generating Password:\n")

generate_password_button = Button(generate_password, text="Click here to generate a password!", button_type='success')
# Show information about each block in the chain
for i, b in enumerate(blockchain.chain):
    print("\n\n Block %d:" % (i+1))
    print("       Hash:              ", b.hash)
    print("     Previous Hash:      ", b.prev_hash)
    print("     Timestamp:          ", datetime.datetime.fromtimestamp(b.time_stamp).strftime("%Y-% m-% s"))
    print("     Transaction Data:     ", b.transaction_data)
    print("     Nonce:             ", b.nonce)
    print("     Merkle Root:       ", b.merkle_root)\ n" " " "Difficulty:   ", b.difficulty)
    print(" Transaction Flags: ", b.flags) # TODO: Implement this once transactions are implemented</s>
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/Bootstrap/3.3.6/css/bootstrap.min.css"/>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.js"></script>
    <style type="text/css">
        .container { margin-top:  50px; }
        </style>
</head>
<body>
<div class="container">
    @yield('content')
</div>

<!-- jQuery -->
<script src="http://code.jquery.com/jquery-2.2.4.min.js"></script>
</body>
</html>

@section('content')
    <h1>Blockchain Information Page</h1>
    <p><a href="/addTransaction ?blockId={{ $id or '' }}&walletAddress= {{ $address or 'null'}}" class="btn btn-primary">Add a
    <p><a href="/addTransaction" class="btn btn-primary my-3">Add a new transaction to the blockchain</a></p>   and
    <p><a href="/addTransaction" class="btn btn-primary">Add a new transaction to the blockchain</a></p /></s>
    <p><a href="/add_Transactions" class="btn btn-primary">Add a new transaction to the blockchain</a></p>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Index</th>
                <th>Timestamp</th>
                <th>Data Hex String</th>
                <th>Transaction Count</th>
                <th>Hash</th>
                <th>Actions</th>
                </tr>
        </thead>
        <tbody>
            @foreach($blocks as $b  => $block)
                <tr id="{{$b}}">
                    <td>{{$loop->index + 1}}</td>
                    <td>{{$block['  transactions'][0]['timestamp']}}</td>
                    <td style="word-wrap: break-word;">{{bin2hex(serialize($block['data']))}}</td>
                    <td>{{count($block['transactions'])}}</td>
                    <td>{{$block['hash']}}</td>
                    <td>
                        <button class="show-transaction btn btn-success" data-toggle="modal " data-target="#viewTransactionModal" value
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewTransactionModal" value
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewTransactionModal" value
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#showTransactionModal" value
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewTransactionModal" value, disabled by default
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewTransactionModal" value={
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewTransactionModal" value = "
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewTransactionModal" value
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewTransactionModal" value
                        <button class="show-transaction btn btn-success" data-toggle="modal" data-target="#viewModal" value={
                        <button onclick="getPrev({{$b}})">Get Previous Block</button>   + <br />
                        <span id="prev_{{ $b }}"></span>
                        
                        <button onclick="   validate({{$b}})">Validate Block</button>  <br />
                        <span id="validated_{{ $b }}"></span> <br />
                        
                        @if ($loop->last)
                            No next block available
                        @else
                            <button onclick="getNext({{$b}}, {{$loop->index+1}})">Get Next Block</button>
                            <span id="next_{{   $b }}"></span>
                        @endif
                    </td>
                </tr>
            @endforeach
        </tbody>
    </table>
<script type="text/javascript">
function getPrev(id){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState ==  4 && this.status == 200) {
            document.getElementById("prev_"+id).innerHTML = this.responseText;
            }
    };
    xhttp.open("GET", "/api/block/"+id+"/previous", true);xhttp.send();
}

function getNext(id, index) {
    window.location.href="/block?page="+(index+1);
}

// Validates a given block by its hash and displays the result in "validated_ID" span element.This is done using AJAX to not refresh the whole page every
function validate(id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {document.getElementById("validated_"+id).innerHTML=this.responseText
    xhttp.onreadystatechange = function() {
        if (this.readyState ==  4 && this.status == 20  && this.status != 204) {
            alert( "Error: " + this.responseText);
            } else if (this.readyState==4 && this.status==204 && this.status != 406) {
                document.getElementById("validated_"+id).innerHTML = "<font color=green>Valid!</font>";
            } else {
                document.getElementById("validated_"+id).innerHTML = "";
            }
    };
    xhttp.open("POST", "/api/validate/"+id, true);xhttp.setRequestHeader('Content-type','   application/json'); xhttp.send();
    xhttp.open("POST", "/validate");
    xhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    // send the data along with the request
    xhttp.send("data="+encodeURIComponent(document.getElementById('txn_'+id).value));
}
</script>
@stop,

@section('footer')
    <div class="row">
        <div class="col-md-8 col-sm-6">
            <ul class="pagination">
            @if($currentPage > 1
                )<li><a href="#" onclick="getNext({{$firstBlock->Id}},{{$currentPage - 1}})"><span aria-hidden="true">&laquo)</span)</a></li>   )</ul>))</div>))</))</))</div>) <div class=")]></div>   <div class=")]></div>   <div class=")]></div> <div class=")]></div) </div>  <div class=")]></div> <div class=")]></div) <div class=")]></div> <div class=")]></div) <div class=")]></div> <div class=")]></div) <div class=")]></div) <div class=")]></div> <div)(class) </))   ))))))))))