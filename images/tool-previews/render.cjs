const sharp=require('sharp'),path=require('path');
(async()=>{for(const key of ['werkplaats','tools-voor-teksten','kladblok','video','screenshot'])await sharp(path.join(__dirname,key+'.svg')).png().toFile(path.join(__dirname,key+'.png'));})();
