h"ref="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-ShareAlike  3.0 Unported License">CC BY-SA 3.0</a>
        </div>
<script type="text/javascript">
    $(document).ready(function(){
        $("#add_button").click(function(){
            var html = $(".clone").html();
            $(".increment").after(html);html.find("select").val($("#select1 option:first").val());});
            $("body").on("click",".remove", function(){
                $(this).parents(".control-group").remove();
                });
                    $('#myTable').DataTable({
                    "paging":   false,
                    "ordering": true,
                    "info":     false,
                    "searching":false
                    });
                });
                </script>
</form> 
<?php  } ?>
</div></div><!-- /.modal-content --></div><!-- /.modal-dialog --></div><!-- /.modal --></div> <!-- ./end of Modal -->
</div></div><!-- /.modal-content --></div><!-- /.modal-dialog --></div><!-- /.modal -->
<!-- Modal Ends Here-->

<!-- Footer Include Starts Here -->
<?php include('footer.php');?>
<!-- Footer Include Ends Here --></body>
</html>
</fancyreports>