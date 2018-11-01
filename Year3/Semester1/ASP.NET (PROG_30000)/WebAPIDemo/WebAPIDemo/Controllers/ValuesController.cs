using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace WebAPIDemo.Controllers
{
    public class ValuesController : ApiController
    {
        public static List<string> myCountries = new List<string>() { "Canada","USA","Poland","Germany"};
        // GET api/values
        public IEnumerable<string> Get()
        {
            return myCountries;
        }

        // GET api/values/5
        public string Get(int id)
        {
            return myCountries[id];
        }

        // POST api/values
        public void Post([FromBody]string value)
        {
            myCountries.Add(value);
        }

        // PUT api/values/5
        public void Put(int id, [FromBody]string value)
        {
            myCountries[id] = value;
        }

        // DELETE api/values/5
        public void Delete(int id)
        {
            myCountries.RemoveAt(id);
        }
    }
}
