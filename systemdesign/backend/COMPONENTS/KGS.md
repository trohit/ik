# Objective
- to show different methods to generate unique keys


# Generators used
- https://truben.no/table/
- https://stackoverflow.com/questions/39378020/how-to-display-table-in-readme-md-file-in-github


<table>
    <tr>
        <th>Identifier Method</th>
        <th>Sample</th>
        <th>Size</th>
        <th>Collision Probability</th>
        <th>Remark</th>
        <th>Pros</th>
        <th>Cons</th>
    </tr>
    <tr>
        <td>Monotonic counter</td>
        <td>1,2,3,...</td>
        <td>Custom</td>
        <td>Uniqueness Guaranteed</td>
        <td>-&nbsp;</td>
        <td>- Simple to use</td>
        <td>- addl mechanism needed to generate concurrently; counterspace needs to be partitioned to use in parallel<br/>- last assigned value needs to be persisted in stable storage</td>
    </tr>
    <tr>
        <td>MD5</td>
        <td></td>
        <td>16 bytes (128 bits)</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>SHA1</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>UUID v4/GUID</td>
        <td>9c5b94b1-35ad-49bb-b118-8e8fc24abf80<br/>8-4-4-4-12&nbsp;</td>
        <td>16 bytes(128 bytes)</td>
        <td>generating 1 billion UUIDs every second for 86 whole years and only then would you have a 50% chance of getting a single collision.</td>
        <td>- digit after 2nd dash indicated uuid version<br/>- Microsoft calls UUID GUID<br/>- Case insensitive</td>
        <td></td>
        <td>- Not sortable<br/>- UUID not easily sortable or time ordered</td>
    </tr>
    <tr>
        <td>ULID</td>
        <td>01ARZ3NDEKTSV4RRFFQ69G5FAV<br/>(t)imstamp x 10 chars + (r)andom x 16 chars</td>
        <td>16 bytes(128 bytes)</td>
        <td></td>
        <td>- Unique Lexicographically Sorted Individual Identifiers, created by Shopify<br/>-&nbsp;1.21e+24 unique ULIDs per ms<br/>- 50% faster than UUID gen retains 128 bit compat with UUID<br/>- 26 hex chars instead of 32 hex chars in UUID<br/>- Uses Crockford Base32 (means ILOU chars not used)<br/>- 48bit TS in ms (works until 10889 AD), 80 bits randomness<br/>- 128 bit compatibility with UUID</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>SnowflakeID</td>
        <td>1765366779879620608<br/>sign_bit_unused(1bit) +<br/>ts_ms_40yrs(41)+<br/>DataCenterID(5) +<br/>machineID/ProcessID(5) +<br/>seq_ctr_resets_every_ms(12)</td>
        <td>8 bytes(64bits)</td>
        <td></td>
        <td>- 10k IDs /sec, resp time &lt; 2ms<br/>- Created at Twitter(X), adopted by Discord &amp; Insta<br/>- 41 bits TS with ms, 10 bits machineID, 12 bits seq_no, 1 bit resvd.<br/>-&nbsp; Insta uses a modified form(41 bits Timestamp,13 bits ShardID,&nbsp; 10bits seq num.<br/>- 41 bits can hold ts in ms upto 70 years i.e 1970-2040, can use custom epoch to extend duration.</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>SonyflakeID</td>
        <td>sign_bit(1bit) +<br/>ts_every_10_ms_174yrs(39bi)&nbsp; +<br/>machine/ProcessID(16bi) +<br/>seq_ctr_resets_every_10ms(8bi)</td>
        <td>8 by (64bi)</td>
        <td></td>
        <td>- Suitable for SMEs<br/>- 8 bits seq id permits 256 ids every 10ms</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>NanoID</td>
        <td>NUp3FRBx-27u1kf1rmOxn<br/>nearly same num of bits for storage as UUID but has a more compact display representation</td>
        <td>126 bits(~16 bytes)</td>
        <td></td>
        <td>- NanoID uses characters (A-Za-z0&ndash;9_-) which is friendly with URLs.<br/>- At just 21 characters, it&rsquo;s more compact than UUID, shaving off 15 characters to be precise (though it&rsquo;s 126 bits versus UUID&rsquo;s 128)</td>
        <td></td>
        <td>- not as widely used as UUID</td>
    </tr>
    <tr>
        <td>ObjectID(MongoDB)</td>
        <td>&nbsp;TS (4 bytes) + rand_val (5 bytes) + counter (3 bytes)</td>
        <td>6502b4ab cf09f864b0 074858<br/>12 bytes or 24 hex chars</td>
        <td></td>
        <td>- 2^40 bits for rand, so chance of collision rare</td>
        <td></td>
        <td></td>
    </tr>
</table>
