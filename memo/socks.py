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
                )<li><a href="#" onclick="getNext({{$firstBlock->Id}},{{$currentPage - 1}})"><span aria-hidden="true">&laquo)</span)</a></li>   )</ul>))</div>))</))</))</div>) <div class=")]></div>   <div class=")]></div>   <div class=")]></div> <div class=")]></div) </div>  <div class=")]></div> <div class=")]></div) <div class=")]></div> <div class=")]></div) <div class=")]></div> <div class=")]></div) <div class=")]></div) <div class=")]></div> <div)(class) </))   )))))))))) )))))    )   ) )) ConnectionRefusedError delete.yield")'anextra,;'('"-\ère;')))))))))))))))))    ))) return)))))) return)))) return) ) return    )) return)))))))))) return)))) return   ))))))) return)))) return)))) return
                        ) <li><a href="#" onclick='getNext("@{{$lastBlock->hash}}", "@{{$currentPage - 1}}")'>&laquo;</a></)(<a href="#" onclick = "getNext("@{{$lastBlock->hash)}", "@{{$currentPage - 1}}"))">&laquo;</a)))</li>) <div class)(class) </div> <div)(class) </div> <div)(class) </div> <div)(class) </div> <div   (class) </div> <div)(class)) </div> <div)(class) </div> <div)(class)) </div))))))   </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class)) </div> <div)(class.'[|(#|#|#|#|#|#|#)]'°])</div> <div)(class)) </div> <div)()</div> <div)(class)) </div> <div)()</
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )<li><a href="#" onclick).click)</a></li>)</div>.sanctuary, property "h.=ref"breaking, property) <div)(class))</div> <div)(class))</div)
                        )<li><a href="#" onclick="getNext({{$firstBlock->id}},{{$currentPage - 1}})" aria-label="Previous"><span aria-hidden))))</)(<a href="#" onclick="){{$firstBlock->id)}">{$currentPage - 1)}</a></li>)</div))</   li>(<li><a href="#" onclick)    )</div></)(<li><a href="#")</div></)(<li><a href)</div></)(<li><a href)</div></)()</div></) <div class=")(<div class=")(<div class=")(<div class=")(<div class=")   (<div class=")(     )))))</div></div></div  <div class=")(<div class=")(<div class=")()")</div></div))</div></div))</div></div></div))</div></div></div)    xlink href)(<div class=")(<div class=")(<div class=")(<div class=")(<div class=")   ()")</div></div))</div></div></div))</div></div></div))</div></div></)      )       )</div></div></div></div)       )       )</div></div></div></div        )</div></div></div  )</div></div></div)></div></div></div)></div></div></div)></div></div></div)></div></div></div)></div></div></div)></div></div></div)></div></div></div)></div></div></div  )</div></div></div)></div></div></div)></)(></div></div></div))></)(></div></div></))   />)</div></div></div></div></div></div)></div></div></div></div></)(></div></div></div></div></div></div)></div></div></div></div></div></div></div)></div></div></div></div></div></div)></div></div></div></div></div)></div></div></div></div></div></div)></div></div></div></div></div)></div></div></div></div></div;
                        )<li><a href="#" onclick='getNext("@{{$lastBlock->hash}}", "@{{$currentPage - 1}}")'>&laquo;</a></  **>)<div></div></div)</div).password_denied AttributeError mean (-|(['open', 'password,keypass'opened, '°', '], [open', 'password,keypass)]))</div></).password)).password)).password)  <div></div></div        ).password)).password)).).password) <div></div></div).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)).password)  <div></div></div).password)).password)).password)).password)).password  <div></div>.password)).password)).password)).password   <div></div>.password)).password)).password <div).password)).password <div). password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div>.password)).password <div).password <div>.password)).password)).password <div>.password)).password <div>.password)).password <div).password <div>.password)).password <div).password <div>.password)).password <div)).,')°à¨ù?'))),-('AttributeError',('AttributeError',('AttributeError',('AttributeError',('KeyError,ValueError',('KeyError,ValueError',('KeyError.TabError',('KeyError.TabError',(';KeyError.TabError',('KeyError.TabError TimeoutError)(|KeyError.TabError'"async"|KeyError.TabError.break|KeyError.TabError influe to error notification,?)|KeyError.TabError').anextension.identifier/key))))    ))),))),)   )`\n'))
                        )
                <li><a href="#" onclick='getNext({{$firstBlock->Id}},{{$currentPage - 1}})' aria-label="Previous"><span aria-hidden = '
                <li><a href="#" onclick="getNext({{$firstBlock->Id}},{{$currentPage - 1}})" aria-label="Previous"><span aria-hidden, href="#
                <li><a href="#" onclick='getNext({{$firstBlock->Id}},{{$currentPage - 1}})' aria-label="Previous"><span aria-hidden
                <li><a href="#" onclick="getPrevious({{$firstBlock->Id}})"><span aria-hidden="true">&laquo;</span></a></li>
                <li><a href="#" onclick="getPrev({{$firstBlock->Id}})"><span aria-hidden="true">&laquo;</span></a></li>
                <li><a href="#" onclick='getPrev({{$firstBlock->Id.AttributeError}})"><span>&laquo;</span></a></
                <li><a href="#" onclick="getPrev({{$firstBlock->Id}})"><span aria-hidden="true">&laquo;</span></a></li>
                <li><a href="#" onclick="getPrevious({{$firstBlock->Id}})"><span aria-hidden="true">&laquo;</span></a></li>
                <li><a href="#" onclick="getPrevious({{$firstBlock->Id}})" aria-label="Previous"><span     aria-hidden="true">&laquo
                <li><a href="#" onclick="getPrevious({{$firstBlock->Id}})"><span aria-hidden="true">&laquo;</span></a></li>
                <li><a href="#" onclick=' getNext({{$transactionCount}},{{$currentPage - 1}})' aria-label="Previous"><span aria-hidden="true">
                <li><a href="#" onclick='getNext({{$transactionCount}},{{$currentPage - 1}})' aria-label="Previous"><span aria-hidden="true
                <li><a href="#" onclick='getNext({{$transactionList[0]->id}},{{$currentPage - 1}})' aria-label="Previous"><span aria_ clicked
                <li><a href="#" onclick='loadPage(1)' aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>
                <li><a href="/transactions?page={{$previousPage}}" aria-label="Previous"><span aria-hidden="true
                <li><a href="/transactions?page={{ $previousPage }}"><span aria-hidden="true">&larr;</span></a></li>
                <li><a href="/transactions?page={{ $previousPage }}"><span aria-hidden="true">&larr;</span></a></li>
                *<li><a href="/transactions?page={{ $previousPage }}"><span aria-hidden="true">&larr;</span    ></a></li>
                *<li><a href="/transactions?page={{ $previousPage }}"><span aria-hidden="true">&larr;</span></a></li>
                *<li><a href="/transactions?page={{ $previousPage }}"><span aria-ria-hidden="true">&rarr;</span>
                Previous Page</a></li>
            @endif
            
            @for ($i =  1; $i <= $lastPage; $i++)
            @if ($currentPage == $i, $i <= $lastPage - 5 and $i >= 7) or ($currentPage > 5 and $i == $currentPage + 2 or $i
                @if ( $i == $currentPage)
                    <li class="active"><a href="#">{{$i}}<span class="sr-only">(current)</span></a></li>
                @else
                <li><a href="/transactions  ?page={{$i}}">{{$i}}</a></li>
                @endif
            @endfor
            
            @if ($currentPage < $lastPage
                        ))
                        Next Page</a></li>
            </ul>
            @endif
        </div>
        <div class="col-md-4 col-sm-6 ">
            <form action="" method="get"id="ref.index]" name="ref.index]0">
                Show  per page:
                <select name="per_page" onchange="document.forms['ref.index
                ].submit()">
                <option value="5"@if($itemsPerPage=='5') selected="
                selected" @endif >5</option>
                <option value="25"@if($itemsPerPage=='25') selected="selected" @endif >25</option>
                <option value="50"@if($itemsPerPage=='50') selected="selected" @endif >50</option>
                <option value="100"@if($itemsPerPage=='100') selected="selected" @endif >100</option>
                </select>
                </form>
        </div>
    </div>
    
    <!-- Table -->
    <table class="table table-hover main-table">
        <thead>
            <tr>
                <th>Date & Time</th>
                <th>Transaction Type</th>
                <th>Amount [USD]</th>
                <th>Balance [USD]</th>
            </tr>
        </thead>
        <tbody>
            @foreach($data as $d)
                <tr>
                    <td>{{date('Y/m/Y')}}</td>
                    <td>{{$d->type}}</td>
                    <td>{{number_format($d->amount,2)}}</td>
                    <td>{{number_format($balances[$loop->iteration -  1],2)}}</td>
                </tr>
            @endforeach
        </tbody>
    </table>
</div>
<div id="pagination">
    {!! $data->appends(Request::except(['page']))->render() !!}
</div>
<!-- Pagination -->

<script type="text/javascript">
$(function(){
    $('.sort').click(function(){
        var url = $(this).attr("id");
        if (url == "desc"){
            window.location.href="/user/transaction?field=created_at&sort=asc";
        }else{
            window.location.href="/user/transaction?field=created_at&sort=desc&" + $("#search").serialize();
        }
    });
});
</script>
@stop, onclick="return confirm('Are you sure to delete this user?');" .ignore 

<a href="#deleteModal" class="btn btn-danger ignore pull-   Right">Delete</a>

<div id="deleteModal" class="modal show">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="   close" data-dismiss="modal" aria-hidden="true">×</button>
                <h4 class="modal-title">Confirm Delete</h4>
            </div>
            <form action="" method="post" id="delForm">
                <input type="hidden" name="_method" value="DELETE"/>
                {{csrf_field()}}
                <div class="modal-body">
                    <p>You are about to delete a User.</p>
                    <p>This cannot be undone. Are you sure?</p>
                </div>
                <div class="modal-footer">
                    <button type="submit" class="btn btn-primary">Yes</button>
                    <button class="btn btn-default" data-dismiss="modal">No</button>
                </div>
            </form>
        </div>
    </div>
</div>

<!-- /Pagination -->
{{$transactions->links()}}
</div>
</div>
</div>
</div>
</div>
</section>
<!-- /Content Section -->
</div>
</div>
<!-- Page Content Ends Here -->
@endsection

@push('scripts')
<script src="/js/jquery.dataTables.min.js"></script>
<script src="/js/datatables/TableTools.min.js"></script>
<script src="/js/datatables import.js"></script>
<script>
$(document).ready(function () {
//    $('#example').DataTable();
    
    $('.deleteBtn').click(function(){ $(this).parent().parent().find('#delForm').attr('action', '/admin/users/' + $(this).val());
    $('.deleteTransaction').click(function (e) {random.seed(); $(this).parent().    find("a").attr("href", "/transaction +" + $(this).
    $('.deleteBtn').click(function (e) {
        e.preventDefault();
        var url = $(this).attr("href");
        $("#myModal").find(".modal-content").unbind().load(url,IOError,function (e) {
            //Application code here....
            $(".yesDelete").click(function(){
                $("#myModal").modal('hide');
                window.location=url;
                });
        })
        
    });
});

function IOError(jqXHR, textStatus, errorThrown){
    console.log("An error occurred!");
}
</script>
@endpush</body></html>