from flask import Flask, Response, render_template
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("Event name")
parser.add_argument("Organised by")
parser.add_argument("Location")
parser.add_argument("Date")
parser.add_argument("Time")

venues = {
"Audi" : [ 26.190935, 91.693063 ],
"Seminar Hall" : [ 26.191146, 91.692469 ],
"L1" : [ 26.188804, 91.691597 ],
"L2" : [ 26.188823, 91.691272 ],
"L3" : [ 26.189143, 91.691296 ],
"L4" : [ 26.189112, 91.691621 ]
}

events = {
	"1":{
		"Event name": "aaa",
		"Organised by": "111",
		"Location": "L1",
		"Date": "9 Oct",
		"Time": "10am",
		"Event ID": "1"
	},
	"2":{
		"Event name": "bbb",
		"Organised by": "222",
		"Location": "Audi",
		"Date": "9 Oct",
		"Time": "12pm",
		"Event ID": "2"	
	},
	"3":{
		"Event name": "ccc",
		"Organised by": "333",
		"Location": "Seminar Hall",
		"Date": "9 Oct",
		"Time": "2pm",
		"Event ID": "3"	
	},
	"4":{
		"Event name": "ddd",
		"Organised by": "444",
		"Location": "Seminar Hall",
		"Date": "9 Oct",
		"Time": "6pm",
		"Event ID": "4"	
	}	
}


## to delete use     del myList[0]
def abort_if_event_doesnt_exist(event_id):
    if event_id not in events:
        abort(404, message="event {} doesn't exist".format(event_id))

class ManageEvent(Resource):
    def get(self, event_id):
        abort_if_event_doesnt_exist(event_id)
        return events[event_id]

    def delete(self, event_id):
        abort_if_event_doesnt_exist(event_id)
        del events[event_id]
        return '', 204

    def put(self, event_id):
        args = parser.parse_args()
        task = {
        "Event name": args["Event name"],
		"Organised by": args["Organised by"],
		"Location": args["Location"],
		"Date": args["Date"],
		"Time": args["Time"],
		"Event ID": str(event_id)	
		}
        events[event_id] = task
        return task, 201

class EventsList(Resource):
    def get(self):
        return events

    def post(self):
        args = parser.parse_args()
        event_id = int(max(events.keys())) + 1
        event_id = str(event_id)
        events[event_id] = {
        "Event name": args["Event name"],
		"Organised by": args["Organised by"],
		"Location": args["Location"],
		"Date": args["Date"],
		"Time": args["Time"],
		"Event ID": event_id	
		}
        return events[event_id], 201


class LocateOnMap(Resource):
	def get(self):
		template_context = dict(events=events, venues=venues)
		return Response(render_template('index.html', **template_context),mimetype='text/html')
		


api.add_resource(ManageEvent, '/event/<string:event_id>')
api.add_resource(EventsList, '/events')
api.add_resource(LocateOnMap, '/event_locations')

#/<string:date>

if __name__ == '__main__':
    app.run(debug=True)