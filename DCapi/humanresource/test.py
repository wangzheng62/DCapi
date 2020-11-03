import json,os

def modal():
    a='''{% macro modal(id="myModal",body=None) %}
    <button type="button" class="btn btn-primary" onclick="showmodal()">
  Launch demo modal111
</button>

    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#{{ id }}">
  Launch demo modal
</button>
<div class="modal fade" id="{{ id }}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" >
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">

                </div>
                <div class="modal-body">
                    {% if body %}
                    {{ body() }}
                    {% endif %}

                </div>
                <div class="modal-footer">

                </div>
            </div>
        </div>
    </div>

    <script>
        function showmodal() {
            $('#{{ id }}').modal({"show":true});

        }

    </script>

{% endmacro %}'''
    return a

print(modal())